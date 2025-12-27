# Contract: billing.invoice.created (v1)

## Purpose
Wird emittiert, wenn eine Rechnung erstellt wurde.

## Topic
`billing.invoice.created`

## Producer
`billing-service`

## Consumers (Beispiele)
- `ods-loader`
- `finance-mart-builder`

## Key (JSON Schema)
Siehe `key.schema.json`

## Payload (JSON Schema)
Siehe `value.schema.json`

## Example Message
Siehe `example.json`

## Compatibility Rules
- Pflichtfelder dürfen nicht entfernt werden.
- Neue optionale Felder sind erlaubt.
- Datentypen dürfen nicht inkompatibel geändert werden.
