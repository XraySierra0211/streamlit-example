import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


# C:\Users\takig\AppData\Roaming\Python\Python311\Scripts\streamlit run streamlit_app.py
# これでローカルホスト
"""
# カテゴリーごとの積み上げ棒グラフ
"""

data = pd.read_csv('shunyu_shishutu.csv')
# st.write(data)

data_1 = data.groupby(['created_at', 'category_code'])['amount'].sum().reset_index()
# st.write(data_1)
# st.write(type(data_1))

pivot_df = data_1.pivot(index='created_at', columns='category_code', values='amount').reset_index()
pivot_df['created_at'] = pd.to_datetime(pivot_df['created_at'], format='%Y/%m/%d')
pivot_df = pivot_df.sort_values('created_at')
st.write(pivot_df)

st.bar_chart(
    pivot_df, x='created_at', y=["Z", "B","C","D","E"]#, color=[]
)