import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

def load_data():

    df = pd.read_csv('top200_movies.csv')
    df['매출액'] = df['매출액'].str.replace(',', '').astype(int)
    df['관객수'] = df['관객수'].str.replace(',', '').astype(int)
    df['스크린수'] = df['스크린수'].str.replace(',', '').astype(int)
    df['상영횟수'] = df['상영횟수'].str.replace(',', '').astype(int)
    return df

st.title("배급사별 천만 영화 점유율")

# 데이터 로드
df = load_data()

# 1000만 관객 이상의 영화만 필터링
df_10m = df[df['관객수'] >= 10000000]

# 배급사별 영화 수 집계
distributor_counts = df_10m.groupby('배급사').size().reset_index(name='count')

# 트리맵 생성
fig = px.treemap(
    distributor_counts,
    path=['배급사'],   # 트리맵의 계층 구조 (여기서는 배급사 단일 항목)
    values='count',     # 각 배급사의 영화 수로 면적 결정
    title="배급사별 천만 영화 점유율"
)
fig.update_traces(textinfo='label+value', textfont_size=20)


st.plotly_chart(fig)