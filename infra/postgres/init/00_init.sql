CREATE SCHEMA IF NOT EXISTS ods;
CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS mart;

CREATE TABLE IF NOT EXISTS ods.load_control (
  id bigserial primary key,
  source_name text not null,
  load_ts timestamptz not null default now(),
  status text not null default 'OK'
);


-- ODS example table for n8n demo
CREATE TABLE IF NOT EXISTS ods.api_posts (
  post_id integer primary key,
  user_id integer not null,
  title text not null,
  body text not null,
  ingested_at timestamptz not null default now()
);


-- ODS example table for Kafka consumer demo
CREATE TABLE IF NOT EXISTS ods.kafka_posts (
  event_id text primary key,
  topic text not null,
  partition integer not null,
  offset bigint not null,
  event_ts timestamptz not null,
  payload jsonb not null,
  ingested_at timestamptz not null default now()
);
