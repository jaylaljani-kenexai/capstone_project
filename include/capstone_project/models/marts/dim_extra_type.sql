with cte as (

    SELECT distinct(extra_type) as extra_type
    from {{source('intermediate','cln_cricket')}}
)


SELECT MD5(extra_type) as extra_type_sk,extra_type
from cte