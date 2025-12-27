# ADR-002: Rolle von Postgres

## Status
Accepted

## Kontext
Postgres ist robust, einfach lokal/homeLab betreibbar und ideal für ODS/Serving.

## Entscheidung
Postgres wird genutzt als:
- ODS/Staging
- Serving für kleine/mittlere Datasets & APIs
- Metadaten/Control Tables (sparsam)

Nicht genutzt als:
- Primäres Lakehouse-Storage für große Volumina
- „All-in-one“ DWH für alles

## Konsequenzen
- Klare Grenzen verhindern späteren „Postgres-Monolithen“.
- Lakehouse bleibt System of Record für große/analytische Workloads.
