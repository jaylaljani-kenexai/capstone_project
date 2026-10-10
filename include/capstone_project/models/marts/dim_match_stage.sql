with cte as (

    SELECT distinct(MATCH_STAGE) as MATCH_STAGE
    from {{source('intermediate','cln_cricket')}}
)


SELECT MD5(MATCH_STAGE) as match_stage_sk,match_stage
from cte