from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import os

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'retries': 0,
}

dag = DAG(
    'test_csv_mount',
    default_args=default_args,
    description='Test CSV mount',
    schedule_interval=None,
    catchup=False,
)

def check_mount():
    """Check if the data directory is mounted"""
    data_dir = '/opt/airflow/data'
    print(f"Checking directory: {data_dir}")
    
    if os.path.exists(data_dir):
        files = os.listdir(data_dir)
        print(f"Found {len(files)} files: {files}")
    else:
        print(f"Directory {data_dir} does not exist!")

check_task = PythonOperator(
    task_id='check_data_mount',
    python_callable=check_mount,
    dag=dag,
)

# Also add a bash task to double-check
bash_check = BashOperator(
    task_id='bash_check_mount',
    bash_command='ls -la /opt/airflow/data',
    dag=dag,
)

check_task >> bash_check