with cte as (

    SELECT distinct VENUE_ID,VENUE_NAME,VENUE_CITY,VENUE_COUNTRY
    from {{source('intermediate','cln_cricket')}}
)


SELECT MD5(VENUE_ID || VENUE_NAME || VENUE_CITY || VENUE_COUNTRY) as venue_sk,venue_id,venue_name,venue_city,venue_country
from cte