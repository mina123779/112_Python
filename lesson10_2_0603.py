import streamlit as st

agree = st.checkbox('我同意') #預設是False 

#checkbox=多選紐 

if agree:
    st.write('棒棒!')