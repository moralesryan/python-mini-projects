import streamlit as st 

st.title("My first streatlit page. ")
st.header("Testing headers. ")
st.write("st. write works as print() it shows text variables and lists ")

name = "Python Tutorial"
st.write(f"Welcome to {name}")

st.info("This is an information box! ")
st.success("This confirms something went well! ")
st.error("This is an error message. ")

