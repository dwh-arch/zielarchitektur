# Demo Walkthrough (v0.2.1)

## Goal
Kafka Topic -> Python Consumer -> Postgres ODS -> (optional dbt/Streamlit)

## Steps
1. `env/local` starten: `docker compose up -d`
2. Producer ausführen: `docker compose run --rm kafka_producer`
3. Prüfen in Postgres:
   - `select count(*) from ods.kafka_posts;`
4. Optional dbt:
   - `dbt run` erzeugt Marts, Streamlit zeigt KPIs
