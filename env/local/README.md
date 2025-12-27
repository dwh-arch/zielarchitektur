# Local Environment (v0.2.1)

## Start
```bash
cp .env.example .env
docker compose up -d
```

## Services
- Postgres: localhost:5432
- Kafka: localhost:9092
- n8n: http://localhost:5678 (Basic Auth aus .env)
- Kafdrop UI: http://localhost:9000
- Kafka consumer: läuft als Container und schreibt nach `ods.kafka_posts`

## Kafka Demo (Topic -> Consumer -> ODS)
1) Umgebung starten: `docker compose up -d`
2) Test-Events senden:
```bash
docker compose run --rm kafka_producer
```
3) In Postgres prüfen:
```sql
select * from ods.kafka_posts order by ingested_at desc limit 20;
```
