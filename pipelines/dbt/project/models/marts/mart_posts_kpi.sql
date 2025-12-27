select
  count(*) as posts_total,
  count(distinct user_id) as users_distinct,
  max(ingested_at) as last_ingest_ts
from {{ ref('stg_api_posts') }}
