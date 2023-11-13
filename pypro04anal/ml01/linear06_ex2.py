import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import scipy.stats
plt.rc('font', family='malgun gothic')
import statsmodels.api
import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor

seatdf = pd.read_csv('../testdata/Carseats.csv')
print(seatdf, seatdf.shape) # 400, 11
print(seatdf.columns)
# ['Sales', 'CompPrice', 'Income', 'Advertising', 'Population', 'Price', 'ShelveLoc', 'Age', 'Education', 'Urban', 'US']
print(seatdf.loc[:,['Sales','CompPrice','Income','Advertising','Population','Price','Age','Education']].corr())
# Sales 와 Price가 상관계수가 제일 높기 떄문에 Price 선택, 독립:Price 종속:Sales

# 단순선형 회귀 모델 작성
lm = smf.ols(formula='Sales ~ Price', data=seatdf).fit()
print(lm.summary())
# p value = 7.618187011913167e-21 < 0.05 이므로 유의한 모델이라 볼 수 있다. 귀무가설 기각 실패
# R-squared = 0.198
# Adj. R-squared = 0.196 모델의 설명력은 다소 떨어짐 -> 변수의 개수 늘리면 설명력 올라감

# plt.scatter(seatdf.Price, seatdf.Sales)
# plt.xlabel('Price')
# plt.ylabel('Sales')
# y_pred = lm.predict(seatdf.Price)
# plt.plot(seatdf.Price, y_pred, c='red')
# plt.show()
# 산포도 그래프로 확인 결과 회귀선을 중심으로 데이터의 분산이 크게 보임.


# 모델 검정
pred=lm.predict(seatdf[:10])
print('실제값 : ', seatdf.Sales[:10].values)
print('예측값 : ', pred[:10].values)

# 실제값 :  [ 9.5       11.22      10.06      7.4        4.15       10.81      6.63       11.85      6.54       4.69]
# 예측값 :  [7.27315296 9.23685464 9.3960737  8.49383238 6.84856881 9.82065785 7.91002918 7.27315296 7.06086088 7.06086088]

# 예측 1 : 임의의 Price로 Sales예측
x_new = pd.DataFrame({'Price':[150.0, 175.0, 200.0]})
pred_new=lm.predict(x_new)
print('Sales 추정 값 : ', '\n', pred_new)
'''
Sales 추정 값 :  
 0    5.680962
1    4.354137
2    3.027311
dtype: float64
'''
'''
# Price를 통한 Sales를 설명하기에 단순 선형회귀 모델상으로는 적합하지 않아보임.
# 다음으로 상관관계가 높은 Advertising항목을 추가하여 다중 선형회귀 모델을 작성.

# 계속해서 추가 해본 결과 다음의 모델이 설명력과 유의성을 어느정도 만족함.
lm_mul = smf.ols(formula='Sales ~ Price+Advertising+Age+Income+CompPrice', data=seatdf).fit()
print(lm_mul.summary())

# p value = 2.70e-64 < 0.05 이므로 유의한 모델이라 볼 수 있다.
# R-squared = 0.540
# Adj. R-squared = 0.534 어느정도 모델을 설명할 수 있음

# 잔차항 도출
pred_df = seatdf[['Price', 'Advertising', 'Age', 'Income', 'CompPrice']]
fitted = lm_mul.predict(pred_df)
residual = seatdf.Sales - fitted
print(residual)
print(sum(residual)) # -2.8475000135586015e-12 잔차의 합은 0에 가까움

# 선형성 검정
sns.regplot(x=fitted, y=residual, lowess=True, line_kws={'color':'red'}) # lowess=True:비모수적 최적모델 추정
plt.plot([fitted.min(), fitted.max()],[0,0], '--',color='blue')
plt.show() # 예측값과 잔차가 곡선을 그리고 있음 - 선형성을 만족하지 못함

# 정규성 검정
ssz = scipy.stats.zscore(residual)
(x,y), _ = scipy.stats.probplot(ssz)
sns.scatterplot(x=x, y=y)
plt.plot([-3,3],[-3,3], '--', color='blue')
plt.show() # 추세선 아래쪽에 존재하는 데이터가 일부 존재하나 추세선을 따라가는 것으로 보임
print('정규성 : ', scipy.stats.shapiro(residual)) # pvalue=0.00044237810652703047 < 0.05 이므로  정규성 만족 못함
# 데이터에 대한 가공이 필요함
'''
lm_mul2 = smf.ols(formula='Sales ~ Price+Advertising+Age+Income', data=seatdf).fit()
print(lm_mul2.summary())
# p value = 1.33e-38 < 0.05 이므로 유의한 모델이라 볼 수 있다.
# R-squared = 0.371
# Adj. R-squared = 0.364 앞의 모델에 비해 설명력이 떨어졌지만 어느정도 설명 가능하다고 보임

# 잔차항 도출
pred_df2 = seatdf[['Price', 'Advertising', 'Age', 'Income']]
fitted2 = lm_mul2.predict(pred_df2)
residual2 = seatdf.Sales - fitted2
print(residual2)
print(sum(residual2)) # -2.185807090882008e-12 잔차의 합은 0에 가까움

# 선형성 검정
sns.regplot(x=fitted2, y=residual2, lowess=True, line_kws={'color':'red'}) # lowess=True:비모수적 최적모델 추정
plt.plot([fitted2.min(), fitted2.max()],[0,0], '--',color='blue')
plt.show() # t

# 정규성 검정
ssz2 = scipy.stats.zscore(residual2)
(x,y), _ = scipy.stats.probplot(ssz2)
sns.scatterplot(x=x, y=y)
plt.plot([-3,3],[-3,3], '--', color='blue')
plt.show() # 추세선 아래쪽에 존재하는 데이터가 일부 존재하나 추세선을 따라가는 것으로 보임
print('정규성 : ', scipy.stats.shapiro(residual2)) # pvalue=0.21268504858016968 > 0.05 이므로  정규성 만족

# 독립성 검정
print('Durbin-Watson : ', 1.931) # 독립성 만족

# 등분산성 검정
sns.regplot(x=fitted2, y=np.sqrt(np.abs(ssz2)), lowess=True, line_kws= {'color':'red'})
plt.show()
# 적색 실선이 수평선에 가깝고 잔차의 분포가 고르게 보임, 등분산성 만족


# 다중 공선성 검정

seatdf2 = seatdf[['Price', 'Advertising', 'Age', 'Income']]
vifdf = pd.DataFrame()
vifdf['vif_value'] = [variance_inflation_factor(seatdf2.values,i)for i in range(seatdf2.shape[1])]
print(vifdf)
# vif 지수가 10보다 작음 따라서 다중공성선 만족


# print(variance_inflation_factor(seatdf.values, 5)) # Price
# print(variance_inflation_factor(seatdf.values, 1)) # Advertising
# print(variance_inflation_factor(seatdf.values, 7)) # Age
# print(variance_inflation_factor(seatdf.values, 3)) # CompPrice
# vifseatdf = pd.DataFrame()
# vifseatdf['vif-value']=[variance_inflation_factor(seatdf.values, i) for i in range(1, 5)]
# print(vifseatdf)

# 모델 검증이 끝난 경우 모델을 저장
# 방법 1
import pickle 
with open('linear06_ex2m.model','wb') as obj: # 저장
    pickle.dump(lm_mul2, obj) 
    
with open('linear06_ex2m.model','rb') as obj: # 읽기
    mymodel = pickle.load(obj) 
    
# 방법 2
import joblib
joblib.dump(lm_mul2, 'linear06_ex')

# 방법 1
'''
import pickle 
with open('linear06_ex2m.model','wb') as obj: # 저장
    pickle.dump(lm_mul2, obj) 
    
with open('linear06_ex2m.model','rb') as obj: # 읽기
    mymodel = pickle.load(obj) 
'''
# 방법 2
# 메모리 절약됨
import joblib 
joblib.dump('linear06_ex2m.model')

mymodel = joblib.load('linear06_ex2m.model')

# 예측 2 : 새로운 'Price', 'Advertising', 'Age', 'Income' 값으로 Sales를 추정
x_new2 = pd.DataFrame({'Price':[200.0,250.0, 170.0], 'Advertising':[11, 15, 13],
                       'Age':[33, 44, 39], 'Income':[65.0, 72.0, 70.0]})
new_pred2 = lm_mul2.predict(x_new2)
print('Sales 추정값 : ', new_pred2.values)
# Sales 추정값 :  [4.14940819 1.30801688 5.86970866]






