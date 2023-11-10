# 단순선형회구분석 모델 생성
# 독립변수(연속형), 종속변수(연속형) : 두 변수는 상관관계가 있어야 하고, 나아가서는 인과관계가 있냐는 가정하에 작성을 한다.
# 회귀분석 : 각각의 데이터에 대한 잔차제곱합이 최소가 되는 방정식을 도출해내는 방법이다. 내부적으로 최소제곱법을 이용

import statsmodels.api as sm 
import numpy as np 
from sklearn.datasets import make_regression 
from astropy.units import yyr

np.random.seed(12)

# 모델 생성 맛보기
print('\n방법1 : make_regression을 사용. 모델 생성 안됨')
x, y, coef = make_regression(n_samples=50, n_features=1, bias=100, coef=True)   # (샘플량, 독립 변수, x절편, 기울기를 보이게 할건지)
print('x, y. coef : ',x,y,coef) # 회귀식 y = wx +b
# 랜덤하게 x값(독립변수)을 생성  [[-1.70073563] [-0.67794537] [ 0.31866529]
# 생성된 x값에 대한 y값(종속변수)을 제시 [ -52.17214291   39.34130801  128.51235594
# 학습 후 수식이 완성(모델) y = wx + b ==> 예측값y = 89.47430739278907 * x + 100
pred_y = 89.47430739278907 * -1.70073563 + 100  # 작성된 모델로 x에 대한 예측값 y를 출력
print('y의 실제값은 ', -52.17214291)
print('x값  -1.70073563에 대한 예측값 y는  ', pred_y) # -52.17214255248879 -> 실제값보다 약간의 오차만 있음
# 회귀분석에서는 95% 신뢰구간안에 있는 y값으로 나타냄. 완전 똑같지 않아도 됨.

new_pred_y = 89.47430739278907 * -1234.5678 + 100
print('내가 궁금한 1234.5678에 대한 예측값은 ',new_pred_y)  # -110362.09883443934

print('\n방법2 : linearRegression을 사용. 모델 생성됨')
xx = x 
yy = y

from sklearn.linear_model import LinearRegression 
model = LinearRegression() 
fit_model = model.fit(xx, yy)
print('기울기(slope) : ',fit_model.coef_) # [89.47430739]
print('절편(bias) : ',fit_model.intercept_) # 100.0
# 예측값 확인 
print(xx[[0]]) 
y_new = fit_model.predict(xx[[0]])
print('y_new : ',y_new) 
y_new2 = fit_model.predict(xx[[12]]) # 정수만 연산하는 듯
print('내가 궁금한 새로운 x값에 대한 예측결과 y는 ', y_new2)

print('\n방법3 : ols을 사용. 모델 생성됨')
# 표를 작성해주기 때문에 보고서작성에 용이하다.
import statsmodels.formula.api as smf
import pandas as pd 
print(xx.shape) # (50, 1) 2차원
x1 = xx.flatten() # 차원축소
print(x1.shape) # (50,) 1차원
y1 = yy
print(y1.shape) # (50,) 1차원

data = np.array([x1, y1])
df = pd.DataFrame(data.T)
df.columns = ['x1','y1']
print(df.head(3), len(df))
model2 = smf.ols(formula='y1~x1', data=df).fit() # 모델 만들어짐
print(model2.summary()) # OLS Regression Results 제공

# 예측값 확인
print(x1[:2]) # 1차원 배열 [-1.70073563 -0.67794537]  
new_df = pd.DataFrame({'x1':[-1.70073563, -0.67794537]}) # 학습할때 값을 유지해야하기 때문에 DataFrame으로 
print(new_df)
new_pred = model2.predict(new_df)
print('예측값 new_pred : ',new_pred)
print('실제값 : ',df.y1[:2])

# 전혀 새로운 독립변수(x) 값에 대한 예측값 확인
new2_df = pd.DataFrame({'x1':[111, -6.612345]})
new2_pred = model2.predict(new2_df)
print('새로운 독립변수(x) 값에 대한 예측값 new_pred : ',new2_pred)
