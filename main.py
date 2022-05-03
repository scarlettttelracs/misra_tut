import streamlit as st
import pandas as pd
import numpy as np

header = st.container()
dataset = st.container()
features = st.container()
modelTraining = st.container()

with header:
    st.title('Welcome!')
    st.header("It is a demo")
    st.subheader("Let's see if it works")
    st.write("By Scarlett")

with dataset:
    st.write("try to plot a line graph")
    df = pd.DataFrame(
        np.random.randn(50, 3),
        columns=('col %d' % i for i in range(3)))
    st.dataframe(df)
    st.line_chart(df)