import streamlit as st
import pandas as pd
import numpy as np

a = [1,2,3,4,5,6,7,8]
n = np.array(a)
nd = n.reshape((2,4))
dic = {
    "name":["hardpope"],
    "empid":["1820154"],
    "city":["kochi"]
}
st.dataframe(dic, width=1000, height=1000)
st.table(dic)
st.write(dic)
