# MLOps Kubeflow Assignment

## Project Overview
This project demonstrates a complete MLOps pipeline for the Boston Housing prediction task (using California Housing dataset as a proxy). It leverages **DVC** for data versioning, **Kubeflow Pipelines (KFP)** for orchestration, and **Jenkins/GitHub Actions** for Continuous Integration.

The pipeline consists of four main components:
1.  **Data Extraction**: Fetches the dataset.
2.  **Data Preprocessing**: Cleans and splits the data into training and testing sets.
3.  **Model Training**: Trains a Random Forest Regressor.
4.  **Model Evaluation**: Evaluates the model and saves metrics (MSE, R2).

## Setup Instructions

### Prerequisites
-   **Minikube**: For running a local Kubernetes cluster.
-   **Kubeflow Pipelines**: Deployed on Minikube.
-   **Python 3.8+**: For local development.
-   **DVC**: For data versioning.

### 1. Environment Setup
Clone the repository:
```bash
git clone https://github.com/Huzaifa-Azam/mlops-kubeflow-assignment.git
cd mlops-kubeflow-assignment
```

Install dependencies:
```bash
pip install -r requirements.txt
pip install "kfp<2.0"
```

### 2. DVC Setup
The data is versioned using DVC. To pull the data:
```bash
dvc pull
```
*Note: This project uses a local remote `../dvc_storage` for demonstration. in a real scenario, this would be an S3 bucket or GCS path.*

## Pipeline Walkthrough

### 1. Compile Components
The pipeline components are defined in `src/pipeline_components.py`. To compile them into YAML files:
```bash
python src/pipeline_components.py
```
This generates:
-   `components/data_extraction.yaml`
-   `components/data_preprocessing.yaml`
-   `components/model_training.yaml`
-   `components/model_evaluation.yaml`

### 2. Compile Pipeline
The pipeline is defined in `pipeline.py`. To compile the full pipeline:
```bash
python pipeline.py
```
This generates `pipeline.yaml`.

### 3. Run on Kubeflow
1.  Open the Kubeflow Pipelines UI (usually at `http://localhost:8080` or via `minikube service`).
2.  Upload `pipeline.yaml`.
3.  Create a run and monitor the steps.

## Continuous Integration
This project uses both **GitHub Actions** and **Jenkins** for CI.

-   **GitHub Actions**: Defined in `.github/workflows/ci.yaml`. Triggers on push to `master`.
-   **Jenkins**: Defined in `Jenkinsfile`. Can be configured as a Pipeline job in Jenkins.

Both pipelines perform the following checks:
1.  Install dependencies.
2.  Compile the pipeline to ensure syntax correctness.
