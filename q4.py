import pandas as pd

### 1. 1차원 데이터를 선언하여 Series형 데이터를 생성하세요.
# 5개의 age 데이터와 이름을 age로 선언해보세요.
age = pd.Series([20, 15, 30, 25, 35], name='age')
print(age,'\n')

### 2. Python Dictionary형 데이터 class_name을 Series형 데이터로 생성하세요.
class_name = {'국어' : 90,'영어' : 70,'수학' : 100,'과학' : 80}
class_series = pd.Series(class_name)
print(class_series,'\n')


### 3. 2차원 데이터를 선언하여 DataFrame형 데이터를 생성하세요.
data_2d = [[0,1],[2,3]]
df = pd.DataFrame(data_2d)
print(df,'\n')