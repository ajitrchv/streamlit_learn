import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

plt.style.use("ggplot")

data = {
    "num":[x for x in range (1,11)],
    "square":[x**2 for x in range (1,11)],
    "twice": [x*2 for x in range (1,11)],
    "thrice": [x*3 for x in range (1,11)]
}
rad  = st.sidebar.radio("Navigation",["About","Home"])
if rad == "Home":
    dff = pd.DataFrame(data = data)

    col = st.sidebar.multiselect("Select a column", dff.columns)
    st.title(col)
    plt.plot(dff['num'],dff[col])
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

if rad == "About":

    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.001)
        progress.progress(i+1)
    st.balloons()

    st.title("You are here in About")
    st.error("Error")
    st.success("Suxess")
    st.info("information")
    st.exception(RuntimeError("A runtime error"))
    st.warning("Warning")

