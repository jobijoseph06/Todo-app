import streamlit as st
from streamlit import session_state

import function

todos = function.get_todo()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    function.write_todo(todos)
    st.session_state["new_todo"] = ""


st.title("MY Todo App")
st.subheader("Todo List")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todo(todos)
        del session_state[todo]
        st.rerun()


st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key="new_todo")


