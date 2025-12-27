# Kafka Producer (v0.2.1)

One-shot producer to send a few demo events to topic `demo.posts`.

## Run
From `env/local`:
```bash
docker compose run --rm kafka_producer
```

Optional env vars:
- KAFKA_TOPIC
- KAFKA_BOOTSTRAP_SERVERS
- PRODUCE_COUNT
