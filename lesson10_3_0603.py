import streamlit as st

genre = st.radio(
    "你最喜歡的電影類型是什麼",
    ('愛情', '驚悚', '動畫'))

if genre == '愛情':
    st.write('你選擇愛情')
elif genre=='驚悚':
    st.write("你選擇驚悚")
elif genre=='動畫':
    st.write("你選擇動畫")