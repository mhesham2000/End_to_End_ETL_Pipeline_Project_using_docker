import sys
sys.path.append('/opt/airflow/api_request')
from insert_records import Insert_record_from_api_to_db
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount



def GetDataFromAPIToDB():
    return Insert_record_from_api_to_db()

default_args = {
    'description': 'A DAG to orchestrate  data ',
    'start_date':datetime(2025,6,20),

}

dag = DAG(
    dag_id="weather_API_DBT_orchestrator",
    default_args=default_args,
    catchup=False,
    schedule=timedelta(minutes=5)
    
)

with dag:

    task1 = PythonOperator(
        task_id = "ingest_data_task",
        python_callable = GetDataFromAPIToDB
    )


    task2 = DockerOperator(
        task_id = 'transform_data_task',
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command='run',
        working_dir='/usr/app',
        mounts=[
            Mount(source='/home/ubuntuwsl/repos/weather-data-project/dbt/my_project',
                  target='/usr/app',
                  type='bind'),
            Mount(source='/home/ubuntuwsl/repos/weather-data-project/dbt/profiles.yml',
                  target='/root/.dbt/profiles.yml',
                  type='bind')
        ],
        network_mode='weather-data-project_my_network',
        docker_url='unix://var/run/docker.sock',
        auto_remove='success'
    )

    task1 >> task2

