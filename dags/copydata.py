from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from datetime import datetime


def copydata():
    try:
            hook=SnowflakeHook(
                            conn_id='snowflake_default'
                        )
    
            sql='''
            COPY INTO CRICKET.RAW.RAW_DATA
            FROM
            (
                SELECT $1,
                       $2,
                       $3,
                       $4,
                       $5,
                       $6,
                       $7,
                       $8,
                       $9,
                       $10,
                       $11,
                       $12,
                       $13,
                       $14,
                       $15,
                       $16,
                       $17,
                       $18,
                       $19,
                       $20,
                       $21,
                       $22,
                       $23,
                       $24,
                       $25,
                       $26,
                       $27,
                       $28,
                       $29,
                       $30,
                       $31,
                       $32,
                       $33,
                       $34,
                       $35,
                       $36,
                       $37,
                       $38,
                       $39,
                       $40,
                       $41,
                       $42,
                       $43,
                       $44,
                       $45,
                       $46,
                       $47,
                       $48,
                       $49,
                       $50,
                       $51,
                       $52,
                       metadata$filename,
                       CURRENT_TIMESTAMP()
                       FROM @CRICKET.RAW.RAW_STAGE/cricket_data.csv

            )

            '''
    
            hook.run(sql)
    except Exception as e:
            print(f"{e}")
            raise
    
    

with DAG (
    dag_id='copydata',
    schedule='@daily',
    start_date=datetime(2026,1,1),
    catchup=False
) as dag:
     p1=PythonOperator(
                 task_id='copydata',
                 python_callable=copydata
             )
     



