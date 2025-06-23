{{config(
    materialized='table',
    unique_key='id'
)}}

with source as (
    SELECT *
    FROM {{ source('dev', 'raw_weather_data') }}
),

de_dup as (
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY time ORDER BY inserted_at desc) AS row_num
    FROM source
)

-- Uncomment the following lines to debug the de_dup CTE
-- select *
-- FROM de_dup



select
    id,
    city,
    temperature,
    weather_description,
    wind_speed,
    time as weather_time_local,
    (inserted_at + (uct_offset || 'hours')::interval) AS inserted_at_local        --enhance: convert UTC to local time  
from de_dup
where row_num = 1       --enhance: keep only the latest record for each time


