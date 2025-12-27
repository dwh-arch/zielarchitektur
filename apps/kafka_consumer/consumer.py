import json
import os
import time
import uuid
from datetime import datetime, timezone

import psycopg2
from kafka import KafkaConsumer

TOPIC = os.getenv("KAFKA_TOPIC", "demo.posts")
BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:29092")
GROUP_ID = os.getenv("KAFKA_GROUP_ID", "ods-loader")
AUTO_OFFSET_RESET = os.getenv("KAFKA_AUTO_OFFSET_RESET", "earliest")
POLL_SECONDS = float(os.getenv("POLL_SECONDS", "1.0"))

PGHOST = os.getenv("PGHOST", "postgres")
PGPORT = int(os.getenv("PGPORT", "5432"))
PGDATABASE = os.getenv("PGDATABASE", os.getenv("POSTGRES_DB", "de_db"))
PGUSER = os.getenv("PGUSER", os.getenv("POSTGRES_USER", "de_user"))
PGPASSWORD = os.getenv("PGPASSWORD", os.getenv("POSTGRES_PASSWORD", "de_pass"))

def pg_conn():
    return psycopg2.connect(
        host=PGHOST, port=PGPORT, dbname=PGDATABASE, user=PGUSER, password=PGPASSWORD
    )

def ensure_ready():
    # Wait for Postgres and Kafka
    for _ in range(60):
        try:
            with pg_conn() as conn:
                with conn.cursor() as cur:
                    cur.execute("select 1;")
            break
        except Exception:
            time.sleep(1)
    else:
        raise RuntimeError("Postgres not reachable")

def main():
    ensure_ready()

    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=BOOTSTRAP,
        group_id=GROUP_ID,
        enable_auto_commit=True,
        auto_offset_reset=AUTO_OFFSET_RESET,
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        key_deserializer=lambda v: v.decode("utf-8") if v else None,
    )

    print(f"[consumer] Listening on topic={TOPIC} bootstrap={BOOTSTRAP} group={GROUP_ID}")

    with pg_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("insert into ods.load_control(source_name, status) values (%s, %s);", (f"kafka:{TOPIC}", "START"))
        conn.commit()

    try:
        while True:
            for msg in consumer.poll(timeout_ms=int(POLL_SECONDS * 1000)).values():
                for record in msg:
                    event_id = str(uuid.uuid4())
                    event_ts = datetime.now(timezone.utc)
                    payload = record.value

                    with pg_conn() as conn:
                        with conn.cursor() as cur:
                            cur.execute(
                                """
                                insert into ods.kafka_posts(event_id, topic, partition, offset, event_ts, payload)
                                values (%s, %s, %s, %s, %s, %s::jsonb)
                                """,
                                (event_id, record.topic, record.partition, record.offset, event_ts, json.dumps(payload)),
                            )
                        conn.commit()
                    print(f"[consumer] wrote event_id={event_id} offset={record.offset}")
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("[consumer] stopping...")
    finally:
        with pg_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("insert into ods.load_control(source_name, status) values (%s, %s);", (f"kafka:{TOPIC}", "STOP"))
            conn.commit()

if __name__ == "__main__":
    main()
