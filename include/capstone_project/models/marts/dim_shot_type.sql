with cte as (

    SELECT distinct(SHOT_TYPE) as SHOT_TYPE
    from {{source('intermediate','cln_cricket')}}
)


SELECT MD5(SHOT_TYPE) as shot_type_sk,shot_type
from cte