import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px


data = pd.read_csv('df_rate.csv')
df = pd.DataFrame(data)

fig = px.scatter(
    df,
    x="expert",
    y="netizen",
    hover_name="movie",
    labels={"expert": "전문가 평점", "netizen": "네티즌 평점"},
    title="전문가 vs 네티즌 평점 산점도"
)
# 천만 영화만 다른색깔로 표현할 수 있을까?
st.plotly_chart(fig)
