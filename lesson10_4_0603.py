import streamlit as st

option = st.selectbox( #下拉式選單 #由上而下重新執行
    '你想怎麼聯繫?',
    ('Email', '電話', '手機'))

st.write('你選擇了:', option)