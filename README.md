# Zielarchitektur Data Engineering / Data Science / AI (Living Repo)

## Why
Dieses Repo ist die **lebendige Zielarchitektur** für eine moderne Data Platform.
Es verbindet **Architektur-Dokumentation**, **deploybare Environments (Local/HomeLab/Cloud)** und **kleine Demos/PoCs**.

## What
Enthält:
- Architektur-Modelle: Lakehouse, ODS, Data Vault, OLAP
- Integration: Quellen, Kafka, Postgres, n8n
- Transformation: dbt, Spark, Databricks
- Experience: Streamlit, Node.js, (Demo-Hosting z.B. pythonanywhere)
- Analytics: Power BI
- AI: Agent Layer + MCP Pattern
- Runtime: Docker, Proxmox

## How
- Doku: `docs/` (Source of Truth)
- Diagramme: `diagrams/mermaid/`
- Local-Setup: `env/local/`
- Pipelines: `pipelines/`
- Apps: `apps/`

## Quickstart (Local)
1) `cp env/local/.env.example env/local/.env`
2) `cd env/local`
3) `docker compose up -d`
4) Postgres: `localhost:5432`, Kafka: `localhost:9092`, n8n: `http://localhost:5678`

## Contributing
- Änderungen via Pull Request
- Architektur-Entscheidungen als ADR in `docs/04_adr/`


## v0.2 Highlights
- n8n Flow (JSONPlaceholder -> Postgres ODS)
- Kafka Event Contract Beispiel unter `contracts/kafka/`
- Streamlit KPI Demo in `apps/streamlit_ui/`


## v0.2.1 Highlights
- Kafka Demo: Topic `demo.posts` -> Python Consumer -> Postgres `ods.kafka_posts`
- One-shot Producer Container: `docker compose run --rm kafka_producer`
