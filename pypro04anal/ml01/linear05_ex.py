# 회귀분석 문제 2) 
# testdata에 저장된 student.csv 파일을 이용하여 세 과목 점수에 대한 회귀분석 모델을 만든다. 
# 이 회귀문제 모델을 이용하여 아래의 문제를 해결하시오.  수학점수를 종속변수로 하자.
#   - 국어 점수를 입력하면 수학 점수 예측
#   - 국어, 영어 점수를 입력하면 수학 점수 예측

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api
import numpy as np
plt.rc('font', family='malgun gothic')

student = pd.read_csv('../testdata/student.csv')
print(student.head(3))
print(student.iloc[:,1:4].corr())

result = smf.ols(formula='국어 ~ 수학', data = student).fit()
print('result 모델 정보 : ', result.summary())
print('result R squared : ', result.rsquared)
print('result p-value : ', result.pvalues[1])  # 8.160795225697216e-05 < 0.05이므로 유의한 모델

'''
# 국어 점수를 입력하면 수학 점수 예측
new_data = pd.DataFrame({'국어':[80,70,65]})
result2 = result.predict(new_data)
print('예측 결과 : ', result2.values)

'''
# 국어, 영어 점수를 입력하면 수학 점수 예측
column_select = "+".join(result.columns.difference(['국어','영어']))
print(column_select)
result3 = smf.ols(formula='수학 ~ ' + column_select, data=result).fit()
print('result3 모델 정보 : ', result3.summary())
plt.show()
