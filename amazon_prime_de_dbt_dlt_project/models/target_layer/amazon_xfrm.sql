{{ config(materialized='table') }}

select 
    cast(show_id as varchar(20)) as show_id,
    type,
    title,
    director,
    "cast",
    country,
    CASE 
    WHEN date_added IS NULL OR date_added = '' THEN NULL
    ELSE cast(date_added as date)
    END as date_added,
    cast(release_year as integer) as release_year,
    rating,
    duration,
    listed_in,
    description
from {{ source('analytics_raw', 'amazon_prime_raw') }}