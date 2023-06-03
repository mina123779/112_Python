import streamlit as st

if st.button('Say hello',key="myButton"): #mybutton=false
    st.write('Why hello there')
else:
    st.write('Goodbye')