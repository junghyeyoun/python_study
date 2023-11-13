# 회귀분석 문제 2) 
# testdata에 저장된 student.csv 파일을 이용하여 세 과목 점수에 대한 회귀분석 모델을 만든다. 
# 이 회귀문제 모델을 이용하여 아래의 문제를 해결하시오.  수학점수를 종속변수로 하자.
#   - 국어 점수를 입력하면 수학 점수 예측
#   - 국어, 영어 점수를 입력하면 수학 점수 예측

import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api
import numpy as np

df=pd.read_csv('../testdata/student.csv', encoding='utf-8')
print(df.head(3))
print(df.iloc[:,1:].corr())

# 국어 점수를 입력하면 수학점수 예측
kor1 = int(input('국어 : '))
result=smf.ols(formula='수학 ~ 국어', data=df).fit()
print(result.summary())  # Prob (F-statistic): 8.16e-05 < 0.05이므로 의미있는 모델
# print('국어:{}에 대한 수학 예측 결과:{}'.format(kor1, 0.5705 * kor1 + 32.1069))

newdf = pd.DataFrame({'국어':[kor1]})
new_pred = result.predict(newdf)
print('국어:{}에 대한 수학 예측 결과:{}'.format(newdf, new_pred[0]))


# 국어, 영어 점수를 입력하면 수학 점수 예측
result2 = smf.ols(formula='수학 ~ 국어 + 영어', data=df).fit()
print('result2 모델 정보 : ', result2.summary()) # Prob (F-statistic): 0.000105 < 0.05이므로 의미있는 모델

kor2 = int(input('국어 : '))
eng = int(input('영어 : '))

# print('국어:{}, 영어:{} 수학점수:{}'.format(kor2,eng, result2.predict(pd.DataFrame({'국어':kor2,'영어':eng}))))

newdf2 = pd.DataFrame({'국어':[kor1],'영어':[eng]})
new_pred2 = result2.predict(newdf2) 
print('국어:{}, 영어:{}에 대한 수학 예측 결과:{}'.format(newdf2['국어'][0] ,newdf2['영어'][0], new_pred2[0]))