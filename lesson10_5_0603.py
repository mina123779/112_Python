import streamlit as st

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'], #四個可以選
    ['Blue', 'Red','Green']) #預設選這幾個

st.write('You selected:', options)