# Diabetes Progression Prediction API (FastAPI)

## Overview
This lab assignment  implements a machine learning API that predicts diabetes disease progression using Linear Regression and serves it through a FastAPI endpoint for predictions.

**Key Changes from Original Lab:**
- **Dataset**: Diabetes dataset (regression) instead of Iris (classification)
- **Algorithm**: Linear Regression instead of Decision Tree Classifier
- **Output**: Continuous disease progression score (25-346 range) instead of categorical classes
- **Features**: 10 normalized features (age, sex, BMI, BP, and 6 blood serum measurements)

## Project Structure
```
diabetes_fastapi/
├── model/
│   └── diabetes_model.pkl          # Trained model (generated after training)
├── src/
│   ├── __init__.py                 # Package initialization
│   ├── data.py                     # Data loading and splitting
│   ├── train.py                    # Model training script
│   ├── predict.py                  # Prediction function
│   └── main.py                     # FastAPI application
├── screenshots/
│   └── api_output.png              # API testing screenshot
├── requirements.txt                # Dependencies
└── README.md                       # This file
```

## Setup & Run

### Create virtual environment
```bash
python -m venv diabetes_env
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Train the Model
```bash
cd src
python train.py
```
This saves the trained model inside the `model/` directory.

### Run the API
```bash
uvicorn main:app --reload
```
Ensure you are in the directory above the `src` directory.

The API will start locally at:
```
http://127.0.0.1:8000
```

### Test the API Using Swagger UI
1. Open your browser
2. Go to: `http://127.0.0.1:8000/docs`
3. The Swagger UI interface will open
4. Click on the `/predict` endpoint
5. Click "Try it out"
6. Replace the request body with the following JSON
7. Click "Execute" to see the prediction response

## Sample JSON Request Body
```json
{
  "age": 0.038,
  "sex": 0.05,
  "bmi": 0.061,
  "bp": 0.021,
  "s1": -0.044,
  "s2": -0.034,
  "s3": -0.043,
  "s4": -0.002,
  "s5": 0.019,
  "s6": -0.017
}
```

**Expected Response:**
```json
{
  "prediction": 204.57761059941167
}
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check - returns `{"status": "healthy"}` |
| POST | `/predict` | Predict diabetes progression based on input features |

## Output Screenshot
FastAPI-output.png is the output. 

