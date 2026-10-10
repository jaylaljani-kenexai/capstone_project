from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from datetime import datetime



def put_file():
    try:
        hook=SnowflakeHook(
                        conn_id='snowflake_default'
                    )
        conn = hook.get_conn()
        cursor = conn.cursor()

        cursor.execute(
            '''
                PUT file:///usr/local/airflow/include/data/cricket_data.csv
                @CRICKET.RAW.RAW_STAGE
                AUTO_COMPRESS=TRUE
            '''
        )

        print(cursor.fetchall())

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"{e}")





with DAG (
    dag_id='put_file',
    schedule='@daily',
    start_date=datetime(2026,1,1),
    catchup=False
) as dag:

    p1=PythonOperator(
            task_id='putfile',
            python_callable=put_file
        )

    
