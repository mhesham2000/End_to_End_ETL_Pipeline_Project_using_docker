import pandas as pd
import psycopg2
import streamlit as st
import plotly.express as px
from streamlit_autorefresh import st_autorefresh


DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "db"
DB_USER = "db_user"
DB_PASS = "db_password"

@st.cache_data(ttl=60)
def get_data(query):
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    df = pd.read_sql(query, conn)
    conn.close()
    return df

st.set_page_config(page_title="Weather Dashboard", layout="wide")
st.title("🌍 Live Weather Dashboard")

# section 1: latest weather report
st.subheader("Latest Weather Report")
report = get_data("SELECT * FROM dev.weather_report ORDER BY inserted_at_local DESC")
st.dataframe(report)

# section 2: daily average
st.subheader("Daily Average by City")
avg = get_data("SELECT * FROM dev.daily_average ORDER BY date DESC")
st.dataframe(avg)

# section 3: temperature chart
st.subheader("Temperature Trend")
fig = px.line(avg, x="date", y="temperature", color="city", markers=True)
st.plotly_chart(fig, use_container_width=True)


st_autorefresh(interval=300000, key="weather_autorefresh")