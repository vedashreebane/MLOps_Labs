
# Airflow Lab: K-Means Clustering Pipeline

## Overview
Using Apache Airflow to orchestrate K-Means clustering on the Vehicle Silhouettes dataset (846 samples, 18 features).

## Project Structure
```
Lab2_airflow/
├── dags/
│   ├── airflow.py          # DAG definition
│   └── src / lab.py              # ML functions
├── data/
│   └── vehicle.csv         # Dataset
├── working_data/           # Model outputs
├── docker-compose.yaml     # Docker config
└── .env                    # Environment variables
```

## Quick Start

### 1. Setup
```bash
mkdir -p ~/Lab2_airflow && cd ~/Lab2_airflow
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.5.1/docker-compose.yaml'
mkdir -p ./dags ./logs ./plugins ./working_data ./data
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

### 2. Configure docker-compose.yaml
- Set `AIRFLOW__CORE__EXECUTOR: LocalExecutor`
- Set `AIRFLOW__CORE__LOAD_EXAMPLES: 'false'`
- Add: `_PIP_ADDITIONAL_REQUIREMENTS: pandas scikit-learn kneed`
- Add volume mounts for `working_data` and `data`
- Comment out `redis` and `airflow-worker` services

### 3. Add Files
- Place `vehicle.csv` in `./data/`
- Create `dags/airflow.py` and `dags/lab.py`

### 4. Launch Airflow
```bash
docker compose up airflow-init
docker compose up
```

### 5. Run Pipeline
1. Open `http://localhost:8080` (airflow/airflow)
2. Enable `mlops_lab_kmeans_clustering` DAG
3. Trigger with play button ▶
4. Monitor:  `load_data` → `preprocess` → `build_model` → `elbow_analysis`

## Pipeline Tasks

**load_data_task** - Load vehicle.csv (846×19) 
**data_preprocessing_task** - Remove Class column, standardize features 
**build_save_model_task** - Train K-Means (K=1-10), save model 
**load_model_task**  - Apply elbow method, find optimal K 

## Results
Check `load_model_task` logs for:
- Optimal clusters (elbow point)
- SSE values for K=1 to K=10
- Model saved to `working_data/model.sav`

## Troubleshooting
- **Tasks queued**: Ensure LocalExecutor, no worker running
- **Import errors**: Move `lab.py` to `dags/` folder
- **File not found**: Check volume mounts
