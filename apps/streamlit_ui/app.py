import os
import psycopg2
import pandas as pd
import streamlit as st

st.title("Zielarchitektur Demo – ODS/Mart Viewer")

host = os.getenv("PGHOST", "localhost")
port = int(os.getenv("PGPORT", "5432"))
dbname = os.getenv("PGDATABASE", "de_db")
user = os.getenv("PGUSER", "de_user")
password = os.getenv("PGPASSWORD", "de_pass")

query = st.text_area("SQL Query", "select * from ods.load_control order by load_ts desc limit 50;")

if st.button("Run"):
    with psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password) as conn:
        df = pd.read_sql(query, conn)
    st.dataframe(df)
