#  Lab 4 — Data Version Control (DVC) with Google Cloud Storage
## Overview
This lab demonstrates how to use **DVC (Data Version Control)** alongside **Git** to manage and version large data files in machine learning projects.
> **The core problem:** Git handles code well, but it breaks down with large data files. DVC solves this by storing data in the cloud and only keeping a small pointer file in Git.

##  How It Works
```
Your Project
    │
    ├── Git ──────────► GitHub
    │                   (stores code + .dvc pointer files)
    │
    └── DVC ──────────► Google Cloud Storage
                        (stores actual data files)
```
## ⚙️ Setup Instructions

### Prerequisites

- Python 3.8+
- Git
- A Google Cloud account with a Storage bucket

### 1. Install DVC with Google Cloud Support

```bash
pip install dvc[gs]
```

### 2. Initialize DVC

```bash
dvc init
git add .dvc
git commit -m "Initialize DVC"
```

### 3. Connect to Google Cloud Storage

```bash
dvc remote add -d myremote gs://<your-bucket-name>
dvc remote modify myremote credentialpath path/to/gcp-key.json
```

> [!WARNING]
> **Never commit your `gcp-key.json` to Git.** Always add it to `.gitignore` before doing `git add`.
> ```bash
> echo "gcp-key.json" >> .gitignore
> ```

---

##  Workflow
### Tracking a New Data File

```bash
# 1. Tell DVC to track the file
dvc add data/bmw_global_sales_2018_2025.csv

# 2. Commit the pointer file to Git (NOT the actual data)
git add data/bmw_global_sales_2018_2025.csv.dvc data/.gitignore
git commit -m "Track dataset with DVC"

# 3. Push the actual data to Google Cloud Storage
dvc push
```

### Getting Data (for collaborators)

```bash
git clone https://github.com/vedashreebane/MLOps_Labs.git
cd MLOps_Labs/Lab4_DVC
dvc pull    # Downloads data from GCS using the .dvc pointer
```

---

## Updating the Dataset
When your data changes, run the same flow — DVC computes a new hash and stores both versions in GCS:
```bash
# Re-add to update the hash in the pointer file
dvc add data/bmw_global_sales_2018_2025.csv

git add data/bmw_global_sales_2018_2025.csv.dvc
git commit -m "Update dataset - v2"

dvc push    # Uploads new version; old version is preserved in GCS
```

---

## Reverting to a Previous Version

```bash
# Step 1: Go back to an old Git commit
git checkout <commit-hash>

# Step 2: Pull the matching data version from GCS
dvc checkout
```

Git holds the history of pointer hashes → DVC fetches the matching data file from GCS.

---
