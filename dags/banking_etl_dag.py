from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def extract_data(**kwargs):
    print("Extracting data...")

def save_raw_csv(**kwargs):
    print("Saving raw CSV...")

def run_dbt(**kwargs):
    result = subprocess.run(
        ["dbt", "run", "--project-dir", "/opt/airflow/dbt"],
        capture_output=True,
        text=True
    )
    print(result.stdout)
    print(result.stderr)

def validate_output(**kwargs):
    print("Validating output...")

with DAG(
    dag_id="banking_etl_dag",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    extract_data_task = PythonOperator(
        task_id="extract_data",
        python_callable=extract_data,
    )

    save_raw_csv_task = PythonOperator(
        task_id="save_raw_csv",
        python_callable=save_raw_csv,
    )

    run_dbt_transform = PythonOperator(
        task_id="run_dbt_transform",
        python_callable=run_dbt,
    )

    validate_output_task = PythonOperator(
        task_id="validate_output",
        python_callable=validate_output,
    )

    extract_data_task >> save_raw_csv_task >> run_dbt_transform >> validate_output_task
