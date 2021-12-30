import streamlit as st

st.title("Registration Form")

first,last = st.columns(2)
first.text_input("First name")
last.text_input("Last Name")

email,mob = st.columns([3,1])
email.text_input("E-Mail")
mob.text_input("Phone Number")

username, password, repass= st.columns(3)
username.text_input("username")
password.text_input("Enter your password",type="password")
repass.text_input("Re Enter the same",type="password")

ch,b,sub=st.columns(3)
ch.checkbox("I agree")
sub.button("Submit")