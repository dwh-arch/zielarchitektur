# Architektur-Prinzipien
1. **Docs-as-Code**: Architektur ist versioniert, reviewbar, reproduzierbar.
2. **Separation of Concerns**: Doku ≠ Runtime ≠ Secrets.
3. **Contracts first**: Events/APIs haben Schemas & Versionierung.
4. **Quality Gates**: Tests sind Teil der Pipeline (dbt tests, checks).
5. **Environment Parity**: Local/HomeLab/Cloud folgen denselben Patterns.
6. **Observability by default**: Logs/Metrics/Lineage sind geplant, nicht nachgerüstet.
7. **Least Privilege**: Security/IAM minimal und auditierbar.
8. **Composable Platform**: Postgres/Kafka/dbt/Spark/Databricks modular.
9. **Data Product Thinking**: Marts/BI/Apps sind Produkte mit Owner & SLA.
10. **Evolution via ADRs**: Jede relevante Entscheidung wird dokumentiert.
