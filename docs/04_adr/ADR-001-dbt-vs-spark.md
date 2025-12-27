# ADR-001: dbt vs Spark (Transformationsstrategie)

## Status
Accepted

## Kontext
Wir haben SQL-lastige Transformationen (Marts/BI) und skalierende Workloads (Streaming, große Datenmengen).

## Entscheidung
- **dbt** ist Standard für: SQL-Transformationen, Marts/BI, Tests, Dokumentation.
- **Spark/Databricks** für: große Volumina, komplexe Verfahren, Streaming, ML/Feature Engineering.

## Begründung
dbt bietet schnelle Iteration, Tests und klare Deployment-Pattern. Spark skaliert besser für große/komplexe Workloads.

## Konsequenzen
- Team braucht beide Skills, aber mit klarer Rollenverteilung.
- Schnittstellen: curated tables/views in ODS/Lakehouse.

## Alternativen
Nur Spark (zu schwergewichtig für BI/Marts), nur dbt (Limits bei Streaming/Skalierung).
