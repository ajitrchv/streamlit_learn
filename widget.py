import streamlit as st
st.title("Widgets")

name = st.text_input("Please enter your name")

address = st.text_area("Adress please")

datex = st.date_input("Date")

timex = st.time_input("Time")

st.radio("Cars",["BMW","Benz","Porsche","Tesla"])

st.selectbox("Cars",["BMW","Benz","Porsche","Tesla"])

st.multiselect("Cars",["BMW","Benz","Porsche","Tesla"])

if st.button("Say my name!"): st.write("Hello",name,'!')
