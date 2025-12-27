# Event Contracts (Kafka)
Empfehlung:
- Topic Naming: `<domain>.<entity>.<event>` (z.B. `billing.invoice.created`)
- Schema Registry (später): Avro/JSON Schema/Protobuf
- Versionierung: backward compatible by default

Template:
- event_name
- version
- producer
- payload schema
- key schema
- examples
