import streamlit as st
import function

todos2 = function.get_todo()

st.title("MY Todo App")
st.subheader("Todo List")

for item in todos2:
    st.checkbox(item)

st.text_input(label="", placeholder="Add new todo...")


