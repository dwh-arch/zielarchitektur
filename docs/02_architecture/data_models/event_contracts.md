# Event Contracts (Kafka)

## Konventionen
- Topic Naming: `<domain>.<entity>.<event>` (z.B. `billing.invoice.created`)
- Keys: stabil und partitionierungsfähig (z.B. `invoice_id`)
- Versionierung: **backward compatible** by default (Additive changes bevorzugt)
- Serialisierung: JSON Schema (v0.2), später Avro/Protobuf + Schema Registry

## Ordner
- Beispiele: `contracts/kafka/`

## Template (Checkliste)
- event_name
- topic
- version
- producer
- consumers
- key schema
- payload schema
- example message
- compatibility rules
