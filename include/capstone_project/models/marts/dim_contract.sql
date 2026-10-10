{{
config   (
materialized='incremental',
unique_key=['DELIVERY_ID'],
incremental_strategy='append'

)
}}


with cte as (

SELECT CONTRACT_ID,CONTRACT_GRADE,ANNUAL_RETAINER_USD,CONTRACT_STATUS,MIN(TRY_TO_DATE(DELIVERY_TIMESTAMP)) as start_date,
null as end_date,
current_timestamp as loaded_at
from {{source('intermediate','cln_cricket')}}

{% if is_incremental() %}

WHERE loaded_at > (SELECT MAX(loaded_at) FROM {{this}} )

{% else %}

WHERE loaded_at > '1900-01-01 00:00:00'

{% endif %}

GROUP BY 1,2,3,4

)


MERGE {{this}} t INTO

USING cte c 
on t.CONTRACT_ID = c.CONTRACT_ID
WHEN MATCHED 
AND t.end_date is null
AND (t.ANNUAL_RETAINER_USD!=c.ANNUAL_RETAINER_USD OR t.CONTRACT_STATUS!=c.CONTRACT_STATUS OR t.ANNUAL_RETAINER_USD!=c.ANNUAL_RETAINER_USD)
THEN

UPDATE SET t.CONTRACT_GRADE=c.CONTRACT_GRADE
t.ANNUAL_RETAINER_USD=c.ANNUAL_RETAINER_USD
t.CONTRACT_STATUS=c.CONTRACT_STATUS
t.end_date=TRY_TO_DATE()

WHEN NOT MATCHED THEN
INSERT (

    CONTRACT_ID,
    CONTRACT_GRADE,
    ANNUAL_RETAINER_USD,
    CONTRACT_STATUS,
    start_date,
    end_date

)
VALUES (
    c.CONTRACT_ID,
    c.CONTRACT_GRADE,
    c.ANNUAL_RETAINER_USD,
    c.CONTRACT_STATUS,
    c.start_date,
    c.end_date
)

