from airflow import DAG
from datetime import date, timedelta,datetime
from airflow.sensors.http_sensor import HttpSensor

default_args = {
    "owner":"Asaph Tinoco",
    "start_date": datetime(2021,4,6),
    "retry_delay":timedelta(minutes=5)
}

with DAG(dag_id="forex_data_pipeline"
        ,schedule_interval="@daily"
        ,default_args=default_args
        ,catchup=False) as dag:

    is_forex_rates_available = HttpSensor(
        task_id="is_forex_dates_available",
        method="GET",
        http_conn_id='forex_api',
        endpoint="latest",
        response_check=lambda response: "rates" in response.text,
        poke_interval=5,
        timeout=20
    )