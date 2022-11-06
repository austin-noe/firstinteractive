import pandas as pd
import streamlit as sl
import altair as alt
import numpy as np

#import batting data
bat_data = pd.read_csv('Batting.csv')

sl.write(bat_data)


sl.sidebar.header("pick two variables for the scatterplot")
x_val = sl.sidebar.selectbox("pick x axis",bat_data.select_dtypes(include=np.number).columns.tolist())
y_val = sl.sidebar.selectbox("pick y axis",bat_data.select_dtypes(include=np.number).columns.tolist())

scatter = alt.Chart(bat_data, title = f"correlation between {x_val} and {y_val}").mark_point().encode(
    alt.X(x_val, title = f"{x_val}"),
    alt.Y(y_val, title = f"{y_val}"),
    tooltip=[x_val, y_val])
sl.altair_chart(scatter, use_container_width=True)

corr = round(bat_data[x_val].corr(bat_data[y_val]),3)
sl.write(f" The correlation between {x_val} and {y_val} is {corr}")
