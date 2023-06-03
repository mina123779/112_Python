import numpy as np #numpy語法
import pandas as pd

scores_array = np.random.randint(50,high=101,size=(50,5)) #numpy語法，最低50最高100，50列5欄

student_dataFrame = pd.DataFrame(data=scores_array, #pandas語法DataFrame
             columns=["國文","英文","數學","地理","社會"],
             index=range(1,51))

print(student_dataFrame) #須加上print讓他列印出來

