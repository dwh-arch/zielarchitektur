CREATE SCHEMA IF NOT EXISTS ods;
CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS mart;

CREATE TABLE IF NOT EXISTS ods.load_control (
  id bigserial primary key,
  source_name text not null,
  load_ts timestamptz not null default now(),
  status text not null default 'OK'
);
