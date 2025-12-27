# n8n

## Zweck
Exportierte n8n Workflows (JSON), damit Flows **reviewbar** und **versioniert** sind.

## v0.2 Beispiel
- `flows/jsonplaceholder_posts_to_postgres.json`
  - holt Posts von JSONPlaceholder
  - schreibt sie in Postgres (`ods.api_posts`)
  - schreibt einen Eintrag in `ods.load_control`

## Import
In n8n UI: **Workflows → Import from File**.
