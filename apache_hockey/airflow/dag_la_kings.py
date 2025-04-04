from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {"owner": "airflow", "start_date": days_ago(1)}

dag = DAG(
    "la_kings_etl",
    default_args=default_args,
    schedule_interval="@daily",
)

extract_task = BashOperator(
    task_id="extract",
    bash_command="python /opt/airflow/dags/etl/extract.py",
    dag=dag,
)

transform_task = BashOperator(
    task_id="transform",
    bash_command="spark-submit /opt/airflow/dags/etl/transform_spark.py",
    dag=dag,
)

load_task = BashOperator(
    task_id="load",
    bash_command="hive -f /opt/airflow/dags/hive/hive_queries.sql",
    dag=dag,
)

extract_task >> transform_task >> load_task
