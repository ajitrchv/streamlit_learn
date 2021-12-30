from altair.vegalite.v4.schema.channels import Tooltip
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

data = pd.DataFrame(
    np.random.randn(100,3),
    columns=['a','b','c']
)
st.set_option('deprecation.showPyplotGlobalUse', False)
plt.scatter(data['a'],data['b'],data['c'])
st.pyplot()



chart = alt.Chart(data).mark_circle().encode(x='a',y='b', tooltip = ['a','b'])

st.graphviz_chart("""
digraph[
    watch -> like
    like -> share
    share -> subscribe
    share -> watch
]
""")

st.altair_chart(chart, use_container_width=True)


#st.line_chart(data)

#st.area_chart(data)

#st.bar_chart(data)

st.image("")
