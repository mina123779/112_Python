import streamlit as st 

if st.button('Say hello',key="myButton"): #mybutton=false #程式都是從上而下讀一次的
    st.write('Why hello there')
else:
    st.write('Goodbye')