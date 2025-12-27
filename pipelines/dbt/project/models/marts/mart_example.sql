select
  example_id,
  date_trunc('day', created_ts) as created_day
from {{ ref('stg_example') }}
