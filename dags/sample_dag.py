from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'sample_dag',
    default_args=default_args,
    description='A simple sample DAG',
    schedule_interval=timedelta(days=1),
    catchup=False,
    tags=['example'],
)

def print_hello():
    """Simple Python function to print hello"""
    print("Hello from Airflow!")
    return "Hello task completed"

def print_date():
    """Print current date"""
    from datetime import datetime
    current_date = datetime.now()
    print(f"Current date and time: {current_date}")
    return current_date

# Define tasks
hello_task = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag,
)

date_task = PythonOperator(
    task_id='print_date',
    python_callable=print_date,
    dag=dag,
)

bash_task = BashOperator(
    task_id='bash_command',
    bash_command='echo "Running bash command in Airflow"',
    dag=dag,
)

# Set task dependencies
hello_task >> date_task >> bash_task