with cte as (

    SELECT distinct MATCH_FORMAT,TOURNAMENT_NAME
    from {{source('intermediate','cln_cricket')}}
)


SELECT MD5(MATCH_FORMAT || TOURNAMENT_NAME) as tournament_sk,match_format,tournament_name
from cte