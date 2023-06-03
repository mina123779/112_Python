import streamlit as st

agree = st.checkbox('我同意') #預設是False

if agree:
    st.write('棒棒!')