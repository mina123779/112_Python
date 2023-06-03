import numpy as np #numpy語法 #np=小名
import pandas as pd #pandas語法 #pd=小名
import streamlit as st #streamlit語法 #st=小名 #原本用print(student_dataFrame) print讓他顯示出來，**改用streamlit網頁顯示**

scores_array = np.random.randint(50,high=101,size=(50,5)) #numpy語法，最低50最高100，50列5欄

student_dataFrame = pd.DataFrame(data=scores_array, #pandas語法DataFrame
             columns=["國文","英文","數學","地理","社會"],
             index=range(1,51))


st.header("3年5班成績表")  #st.=streamlit語法
#st.table(data=student_dataFrame)  #st.=streamlit語法  #網頁不可下拉
st.dataframe(data=student_dataFrame)  #st.=streamlit語法 #網頁可下拉

#終端機輸入Streamlit run lesson9_1_0603.py(檔名)讓他跑