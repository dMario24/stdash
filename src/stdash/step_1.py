import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from stdash.data import load_data


# https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config
st.set_page_config(
    page_title="CNN JOB MON",
    layout="centered",
    page_icon=":shark:",
    initial_sidebar_state="expanded")

# https://docs.streamlit.io/get-started/fundamentals/additional-features
st.markdown("# STEP 1 🎈")
st.sidebar.markdown("# STEP 1 🎈")

st.title('CNN JOB MON')

df = load_data()

df['request_time'] = pd.to_datetime(df['request_time']).dt.floor('30min')
df['prediction_time'] = pd.to_datetime(df['prediction_time']).dt.floor('30min')

r_hourly_counts = df.groupby('request_time').size()
p_hourly_counts = df.groupby('prediction_time').size()


plt.bar(r_hourly_counts.index, r_hourly_counts.values, label='request', width=0.015)
plt.plot(p_hourly_counts.index, p_hourly_counts.values, color='red', marker='o', label='prediction')

plt.title('request & prediction per hour')

plt.ylabel('count')
plt.xticks(rotation=45)

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H'))

# 화면에 그리기
st.pyplot(plt)
