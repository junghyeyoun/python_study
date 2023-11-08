from dask.dataframe.reshape import pivot_table
print('문제1')
import numpy as np
data = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])

print(data)
print(data[::-1, ::-1])

print('문제2')
'''
import seaborn as sns
titanic = sns.load_dataset('titanic')
print(titanic.head())
print(titanic.columns)
#result = titanic.pivot_table(index='sex', columns='class', values='survived', aggfunc='mean')
# print(result)
print(titanic.pivot_table(index='sex', columns='class', values='survived', aggfunc='mean'))
'''
print('문제7')
from pandas import DataFrame
frame = DataFrame({'bun':[1,2,3,4], 'irum':['aa','bb','cc','dd']},
                  index=['a','b', 'c','d'])

print(frame.T) 
frame2 = frame.drop('d')  
print(frame2)

print('문제9')
import pandas as pd

data = {
    'juso':['강남구 역삼동', '중구 신당동', '강남구 대치동'],
    'inwon':[23, 25, 15]
}

df = pd.DataFrame(data)

# 'juso' 칼럼의 값을 공백을 기준으로 분할하여 0번째 자료를 Series로 저장
results = pd.Series([x.split()[0] for x in df['juso']])

print(results)

print('문제10')
import numpy as np

x = np.array([1, 2, 3, 4, 5])  # 1차원 배열
y = np.array([1, 2, 3]).reshape(-1, 1)  # 2차원 배열 (3행 1열)

result = x + y

print(result)

print('문제 13')
from pandas import DataFrame

data = {"a": [80, 90, 70, 30], "b": [90, 70, 60, 40], "c": [90, 60, 80, 70]}
# 칼럼(열)의 이름 변경
df = DataFrame(data, columns=["국어", "영어", "수학"])
print(df)
# 1) 모든 학생의 수학 점수 출력
math_scores = df["수학"]
print("1) 모든 학생의 수학 점수:")
print(math_scores)

# 2) 모든 학생의 수학 점수의 표준편차 출력
math_std = df["수학"].std()
print("\n2) 모든 학생의 수학 점수의 표준편차:", math_std)

# 3) 모든 학생의 국어와 영어 점수를 DataFrame type으로 출력
korean_english_scores = df[["국어", "영어"]]
print("\n3) 모든 학생의 국어와 영어 점수:")
print(korean_english_scores)


print('문제 15')

import pandas as pd 
import scipy.stats as stats

# 귀무 : 등급(Pclass)에 따라 생존율(Survived)이 차이가 없다.
# 대립 : 등급(Pclass)에 따라 생존율(Survived)이 차이가 있다.
titanic = pd.read_csv('../testdata/titanic_data.csv')

ctab = pd.crosstab(index=titanic['Pclass'], columns=titanic['Survived'])

chi2, p, dof, _ = stats.chi2_contingency(ctab)
print('chi2:{}, p:{}, dof:{}'.format(chi2, p, dof))

# 판정 : p-value가 4.549251711298793e-23 < 0.05 이므로 귀무가설을 기간한다.
# 따라서 등급(Pclass)에 따라 생존율(Survived)이 차이가 있다.