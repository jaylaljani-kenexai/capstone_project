with cte as (

    SELECT distinct(SHOT_REGION) as SHOT_REGION
    from {{source('intermediate','cln_cricket')}}
)


SELECT MD5(SHOT_REGION) as shot_region_sk,shot_region
from cte