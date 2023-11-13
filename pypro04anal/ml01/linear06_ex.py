# 회귀분석 문제 3)    
# kaggle.com에서 carseats.csv 파일을 다운 받아 (https://github.com/pykwon 에도 있음) Sales 변수에 영향을 주는 변수들을 선택하여 선형회귀분석을 실시한다.
# 변수 선택은 모델.summary() 함수를 활용하여 타당한 변수만 임의적으로 선택한다.
# 회귀분석모형의 적절성을 위한 조건도 체크하시오.
# 완성된 모델로 Sales를 예측.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api
import numpy as np
plt.rc('font', family='malgun gothic')

advdf = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/Carseats.csv')
print(advdf.head(3))
print(advdf.columns)
print('r : \n', advdf.loc[:,['Sales','Income','Advertising','Price','Age']].corr()) 
# 상관계수 그나마 높은 Price와 Advertising으로 선택
lm_mul = smf.ols(formula = 'Sales ~ Price+Advertising', data=advdf).fit()
print(lm_mul.summary()) 
# Prob (F-statistic): 2.87e-29 < 0.05 귀무가설 기각 실패 -> 유의한 모델 / R-squared: 0.282

print('/n/n모델 검정')
pred = lm_mul.predict(advdf[:10])
print('실제값 : ',advdf.Sales[:10].values)
print('예측값 : ',pred[:10].values)


print('\n\n예측 : 새로운  Price와 Advertising 값으로 Sales 추정')
x_new = pd.DataFrame({'Price':[85, 98, 130],'Advertising':[10,15,20]})
new_pred = lm_mul.predict(x_new)
print('Sales 추정값 ', new_pred.values)

