# Streamlit UI (v0.2 KPI Demo)

## Prereqs
- Postgres läuft (Local: `env/local/docker-compose.yml`)
- Optional: dbt wurde ausgeführt, damit `mart.mart_posts_kpi` existiert

## Start
```bash
pip install streamlit psycopg2-binary pandas
streamlit run app.py
```

## Data Load via n8n
1) `docker compose up -d` in `env/local`
2) n8n öffnen: http://localhost:5678
3) Credential "Postgres Local" anlegen (Host: `postgres`, Port `5432`, DB/User/Pass aus `.env`)
4) Workflow importieren: `pipelines/orchestration/n8n/flows/jsonplaceholder_posts_to_postgres.json`
5) Webhook testen: Workflow aktivieren und Webhook URL aufrufen
