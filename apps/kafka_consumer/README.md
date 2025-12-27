# Kafka Consumer -> Postgres ODS (v0.2.1)

## Purpose
Liest Events aus Kafka Topic `demo.posts` und schreibt sie nach Postgres:
- `ods.kafka_posts` (raw event envelope)
- `ods.load_control` (1 Eintrag pro Run, optional)

## Run (via docker compose)
Im lokalen Environment ist der Service `kafka_consumer` integriert.

Start:
```bash
cd env/local
docker compose up -d
```

Topic wird durch `kafka_init` erstellt.

## Produce test events
Siehe `apps/kafka_producer/` oder nutze Kafdrop/UI.
