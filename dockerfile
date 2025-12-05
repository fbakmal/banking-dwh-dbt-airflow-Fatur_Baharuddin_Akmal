FROM apache/airflow:2.7.1

# Install dbt sebagai user airflow
USER airflow

RUN pip install --user dbt-core dbt-postgres

ENV PATH="/home/airflow/.local/bin:${PATH}"
