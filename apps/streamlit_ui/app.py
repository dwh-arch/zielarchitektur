import os
import psycopg2
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Zielarchitektur KPI Demo", layout="wide")
st.title("Zielarchitektur Demo – KPI Dashboard (v0.2)")

host = os.getenv("PGHOST", "localhost")
port = int(os.getenv("PGPORT", "5432"))
dbname = os.getenv("PGDATABASE", "de_db")
user = os.getenv("PGUSER", "de_user")
password = os.getenv("PGPASSWORD", "de_pass")

def q(sql: str) -> pd.DataFrame:
    with psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password) as conn:
        return pd.read_sql(sql, conn)

col1, col2, col3 = st.columns(3)

kpi_sql = "select posts_total, users_distinct, last_ingest_ts from mart.mart_posts_kpi;"
fallback_sql = "select count(*) as posts_total, count(distinct user_id) as users_distinct, max(ingested_at) as last_ingest_ts from ods.api_posts;"

try:
    kpi = q(kpi_sql).iloc[0]
except Exception:
    kpi = q(fallback_sql).iloc[0]

col1.metric("Posts total", int(kpi["posts_total"]))
col2.metric("Distinct users", int(kpi["users_distinct"]))
col3.metric("Last ingest", str(kpi["last_ingest_ts"]))

st.divider()

st.subheader("Latest ingested posts (ODS)")
df = q("select post_id, user_id, title, ingested_at from ods.api_posts order by ingested_at desc limit 50;")
st.dataframe(df, use_container_width=True)

st.divider()
st.subheader("Ad-hoc SQL")
query = st.text_area("SQL Query", "select * from ods.load_control order by load_ts desc limit 50;")
if st.button("Run query"):
    st.dataframe(q(query), use_container_width=True)
