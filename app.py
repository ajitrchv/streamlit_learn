import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import plotly as go
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np 

st.set_option('deprecation.showPyplotGlobalUse', False)
data = pd.read_csv("data/username.csv")
x = np.array(data['YearsExperience']).reshape(-1,1)
lr  = LinearRegression()
lr.fit(x,np.array(data['Salary']))

st.title("Salary Predictor")

nav = st.sidebar.radio("Navigation",["Home","Prediction","Contribute"])

if nav == "Home":
    st.image("data/sal.png",width = 800)
    if st.checkbox("Show Table"):
        st.table(data)
    graph = st.selectbox("Graph kind?",["interactive","non-interactive"])
    
    val = st.slider("Filter data using years:",0,20)
    data = data.loc[data["YearsExperience"]>=val]
    
    if graph == "non-interactive":
        plt.figure(figsize = (10,5))
        plt.scatter(data["YearsExperience"], data["Salary"])
        plt.ylim(0)
        plt.xlabel("YearsExperience")
        plt.ylabel("Salary")
        plt.tight_layout()
        st.pyplot()
    if graph == "interactive":
        layout = go.Layout(
        xaxis = dict(range=[0,16]),
        yaxis = dict(range=[0, 50000])
    )
        fig = go.Figure(data=go.Scatter(x=data["YearsExperience"], y=data["Salary"], mode='markers'),layout = layout)
        st.plotly_chart(fig)

    

if nav == "Prediction":
    st.header("Know your Salary")
    val = st.number_input("Enter you exp",0.00,20.00,step = 0.25)
    val = np.array(val).reshape(1,-1)
    pred = lr.predict(val)[0]

    if st.button("Predict"):
        st.success(f"Your predicted salary is {round(pred)}")

if nav == "Contribute":
    st.header("Contribute to our dataset")
    ex = st.number_input("Enter your Experience",0.0,20.0)
    sal = st.number_input("Enter your Salary",0.00,1000000.00,step = 1000.0)
    if st.button("submit"):
        to_add = {"YearsExperience":[ex],"Salary":[sal]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("data/Salary_Data.csv",mode='a',header = False,index= False)
        st.success("Submitted")