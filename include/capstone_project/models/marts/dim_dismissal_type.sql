with cte as (

    SELECT distinct(DISMISSAL_TYPE) as DISMISSAL_TYPE
    from {{source('intermediate','cln_cricket')}}
)


SELECT MD5(DISMISSAL_TYPE) as dismissal_type_sk,dismissal_type
from cte