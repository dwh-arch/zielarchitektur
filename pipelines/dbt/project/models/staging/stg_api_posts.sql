with src as (
  select
    post_id,
    user_id,
    title,
    body,
    ingested_at
  from ods.api_posts
)
select * from src
