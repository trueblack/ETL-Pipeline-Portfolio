from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
import pandas as pd

# Default arguments
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
    'data_loading_pipeline',
    default_args=default_args,
    description='Load data into PostgreSQL',
    schedule_interval=None,  # Manual trigger only
    catchup=False,
    tags=['data-loading', 'postgres'],
)

def load_sample_data():
    """Load sample data into PostgreSQL"""
    # Create sample data (you can replace this with CSV reading, API calls, etc.)
    sample_data = [
        ('John Doe', 25, 'john@email.com', '2024-01-01'),
        ('Jane Smith', 30, 'jane@email.com', '2024-01-02'),
        ('Bob Johnson', 35, 'bob@email.com', '2024-01-03'),
        ('Alice Brown', 28, 'alice@email.com', '2024-01-04'),
        ('Charlie Wilson', 32, 'charlie@email.com', '2024-01-05'),
    ]
    
    # Get PostgreSQL hook
    postgres_hook = PostgresHook(postgres_conn_id='postgres_default')
    
    # Insert data
    insert_sql = """
    INSERT INTO users (name, age, email, created_date) 
    VALUES (%s, %s, %s, %s)
    """
    
    for row in sample_data:
        postgres_hook.run(insert_sql, parameters=row)
    
    print(f"Loaded {len(sample_data)} records into users table")

def load_from_csv():
    """Example: Load data from CSV file"""
    # This assumes you have a CSV file in your dags folder
    # You can modify this to read from any source
    
    postgres_hook = PostgresHook(postgres_conn_id='postgres_default')
    
    # Example CSV data (in real scenario, you'd use pd.read_csv('/path/to/file.csv'))
    data = {
        'product_name': ['Widget A', 'Widget B', 'Widget C'],
        'price': [19.99, 29.99, 39.99],
        'category': ['Electronics', 'Electronics', 'Tools']
    }
    
    df = pd.DataFrame(data)
    
    # Insert data
    for _, row in df.iterrows():
        insert_sql = """
        INSERT INTO products (name, price, category) 
        VALUES (%s, %s, %s)
        """
        postgres_hook.run(insert_sql, parameters=(row['product_name'], row['price'], row['category']))
    
    print(f"Loaded {len(df)} products from CSV")

# Create tables
create_tables = PostgresOperator(
    task_id='create_tables',
    postgres_conn_id='postgres_default',
    sql="""
    -- Create users table
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INTEGER,
        email VARCHAR(100),
        created_date DATE
    );
    
    -- Create products table
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        price DECIMAL(10,2),
        category VARCHAR(50)
    );
    """,
    dag=dag,
)

# Load sample user data
load_users = PythonOperator(
    task_id='load_user_data',
    python_callable=load_sample_data,
    dag=dag,
)

# Load product data
load_products = PythonOperator(
    task_id='load_product_data',
    python_callable=load_from_csv,
    dag=dag,
)

# Set task dependencies
create_tables >> [load_users, load_products]