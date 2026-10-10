from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from datetime import datetime



def create_file_format():
    try:
        hook=SnowflakeHook(
                        conn_id='snowflake_default'
                    )

        sql='''
        CREATE OR REPLACE FILE FORMAT CRICKET.RAW.CSV_FORMAT
        TYPE=CSV
        FIELD_DELIMITER=','
        FIELD_OPTIONALLY_ENCLOSED_BY = '"'
        SKIP_HEADER=1
        NULL_IF=('NULL','','null')
        '''

        hook.run(sql)
    except Exception as e:
        print(f"{e}")


def create_stage():
    try:
        hook=SnowflakeHook(
                                conn_id='snowflake_default'
                            )

        sql='''
        CREATE OR REPLACE STAGE CRICKET.RAW.RAW_STAGE
        FILE_FORMAT = CRICKET.RAW.CSV_FORMAT
        '''
        hook.run(sql)
    except Exception as e:
        print(f"{e}")


with DAG (
    dag_id='create_stage',
    schedule='@daily',
    start_date=datetime(2026,1,1),
    catchup=False
) as dag:

    p1=PythonOperator(
            task_id='create_file_format',
            python_callable=create_file_format
        )

    p2=PythonOperator(
                task_id='create_stage',
                python_callable=create_stage
            )

    p1>>p2
    
