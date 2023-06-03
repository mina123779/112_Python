import streamlit as st

def button_click():
    st.write(st.session_state)

if st.button("say Hello!",key='myButton',on_click=button_click): #myButton=False #程式都是從上而下讀一次的
    st.write("Why hello there")
else:
    st.write("Goodbye")