# Import necessary libraries and modules
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from src.lab import load_data, data_preprocessing, build_save_model, load_model_elbow
from airflow import configuration as conf

# Enable pickle support for XCom, allowing data to be passed between tasks
conf.set('core', 'enable_xcom_pickling', 'True')

# Define default arguments for your DAG
default_args = {
    'owner': 'vedashree bane',  # Change this to your name
    'start_date': datetime(2026, 2, 14),
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

# Create a DAG instance
dag = DAG(
    'mlops_lab_kmeans_clustering',
    default_args=default_args,
    description='K-Means Clustering Pipeline',
    schedule_interval=None,  # Manual triggering
    catchup=False,
)

# Task 1: Load data
load_data_task = PythonOperator(
    task_id='load_data_task',
    python_callable=load_data,
    dag=dag,
)

# Task 2: Preprocess data
data_preprocessing_task = PythonOperator(
    task_id='data_preprocessing_task',
    python_callable=data_preprocessing,
    op_args=[load_data_task.output],
    dag=dag,
)

# Task 3: Build and save model
build_save_model_task = PythonOperator(
    task_id='build_save_model_task',
    python_callable=build_save_model,
    op_args=[data_preprocessing_task.output, "model.sav"],
    provide_context=True,
    dag=dag,
)

# Task 4: Load model and perform elbow analysis
load_model_task = PythonOperator(
    task_id='load_model_task',
    python_callable=load_model_elbow,
    op_args=["model.sav", build_save_model_task.output],
    dag=dag,
)

# Set task dependencies
load_data_task >> data_preprocessing_task >> build_save_model_task >> load_model_task

# Command-line interaction
if __name__ == "__main__":
    dag.cli()