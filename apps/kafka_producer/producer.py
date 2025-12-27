import json
import os
import time
from datetime import datetime, timezone
from kafka import KafkaProducer

TOPIC = os.getenv("KAFKA_TOPIC", "demo.posts")
BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:29092")
COUNT = int(os.getenv("PRODUCE_COUNT", "20"))

producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    key_serializer=lambda v: v.encode("utf-8") if v else None,
)

print(f"[producer] sending {COUNT} events to {TOPIC} via {BOOTSTRAP}")

for i in range(1, COUNT + 1):
    payload = {
        "event_name": "demo.post.created",
        "version": 1,
        "ts": datetime.now(timezone.utc).isoformat(),
        "post_id": i,
        "user_id": (i % 10) + 1,
        "title": f"Demo Post {i}",
        "body": "hello from kafka producer"
    }
    producer.send(TOPIC, key=str(i), value=payload)
    if i % 5 == 0:
        producer.flush()
    time.sleep(0.05)

producer.flush()
print("[producer] done")
