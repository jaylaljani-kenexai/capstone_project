from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from datetime import datetime



def create_table():
    try :
        hook=SnowflakeHook(
                conn_id='snowflake_default'
            )
        
        sql='''
            CREATE OR REPLACE TABLE
            CRICKET.RAW.RAW_DATA
            (
                delivery_id VARCHAR,
                delivery_timestamp VARCHAR DEFAULT NULL,
                innings_no VARCHAR DEFAULT NULL,
                over_no VARCHAR DEFAULT NULL,
                ball_in_over VARCHAR DEFAULT NULL,
                runs_off_bat VARCHAR DEFAULT NULL,
                extra_type VARCHAR DEFAULT NULL,
                extra_runs VARCHAR DEFAULT NULL,
                total_runs VARCHAR DEFAULT NULL,
                is_wicket VARCHAR DEFAULT NULL,
                dismissal_type VARCHAR DEFAULT NULL,
                ball_speed_kmph VARCHAR DEFAULT NULL,
                non_striker_id VARCHAR DEFAULT NULL,
                shot_type VARCHAR DEFAULT NULL,
                shot_region VARCHAR DEFAULT NULL,
                match_id VARCHAR DEFAULT NULL,
                match_date VARCHAR DEFAULT NULL,
                match_format VARCHAR DEFAULT NULL,
                tournament_name VARCHAR DEFAULT NULL,
                season VARCHAR DEFAULT NULL,
                match_stage VARCHAR DEFAULT NULL,
                toss_decision VARCHAR DEFAULT NULL,
                venue_id VARCHAR DEFAULT NULL,
                venue_name VARCHAR DEFAULT NULL,
                venue_city VARCHAR DEFAULT NULL,
                venue_country VARCHAR DEFAULT NULL,
                batting_team_id VARCHAR DEFAULT NULL,
                batting_team_name VARCHAR DEFAULT NULL,
                bowling_team_id VARCHAR DEFAULT NULL,
                bowling_team_name VARCHAR DEFAULT NULL,
                batsman_id VARCHAR DEFAULT NULL,
                batsman_name VARCHAR DEFAULT NULL,
                batsman_dob VARCHAR DEFAULT NULL,
                batsman_nationality VARCHAR DEFAULT NULL,
                batting_hand VARCHAR DEFAULT NULL,
                batsman_role VARCHAR DEFAULT NULL,
                batsman_email VARCHAR DEFAULT NULL,
                batsman_phone VARCHAR DEFAULT NULL,
                batsman_icc_rating VARCHAR DEFAULT NULL,
                bowler_id VARCHAR DEFAULT NULL,
                bowler_name VARCHAR DEFAULT NULL,
                bowler_nationality VARCHAR DEFAULT NULL,
                bowling_style VARCHAR DEFAULT NULL,
                bowler_icc_rating VARCHAR DEFAULT NULL,
                contract_id VARCHAR DEFAULT NULL,
                contract_grade VARCHAR DEFAULT NULL,
                annual_retainer_usd VARCHAR DEFAULT NULL,
                contract_status VARCHAR DEFAULT NULL,
                drs_review_id VARCHAR DEFAULT NULL,
                drs_reviewed_by VARCHAR DEFAULT NULL,
                drs_original_decision VARCHAR DEFAULT NULL,
                drs_outcome VARCHAR DEFAULT NULL,
                FILENAME VARCHAR DEFAULT NULL,
                TIMESTAMP VARCHAR DEFAULT NULL
            )
        '''

        hook.run(sql)
    except Exception as e:
        print(f"{e}")
        raise
with DAG (
    dag_id='create_table',
    schedule='@daily',
    start_date=datetime(2026,1,1),
    catchup=False
) as dag:

    p1=PythonOperator(
        task_id='create_table',
        python_callable=create_table
    )


    