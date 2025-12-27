# C4 Context/Container
Siehe Diagramm: `diagrams/mermaid/c4_container.mmd`

Kurzbeschreibung:
- Kafka für Event/Streaming, n8n für Integrations-/Automationsflows.
- Postgres als ODS/Staging/Serving (bewusst begrenzt – siehe ADR-002).
- dbt als SQL-Transformation/Quality Gate, Spark/Databricks für skalierende Workloads.
- Lakehouse für Zonen (Bronze/Silver/Gold) und Data Science/AI.
- OLAP/Marts als BI-serving Schicht (Power BI + Streamlit).
- Agent/MCP als Pattern für Tool-Integration und „AI-assisted ops“.
