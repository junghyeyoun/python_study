#  sklearn의 분류모델은 output이 연속형인 예측 모델도 제공
import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression 
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor 
from sklearn.metrics import r2_score

adver = pd.read_csv('../testdata/Advertising.csv', usecols=[1,2,3,4])
print(adver.head(3), adver.shape)
print(adver.corr(method='pearson'))

x = np.array(adver.loc[:,'tv':'newspaper'])
y = np.array(adver.sales)
print(x[:3]) # 메트릭스
print(y[:3]) # 백터

print('LinearRegression ----------------------')
lmodel = LinearRegression().fit(x,y)
lpred = lmodel.predict(x)
print('LinearRegression pred : ',lpred[:5])
print('LinearRegression real: ',y[:5])
print('결정 계수 : ',r2_score(y, lpred))

print('RandomForestRegressor ----------------------')
rmodel = RandomForestRegressor(criterion='squared_error').fit(x,y)
rpred = rmodel.predict(x)
print('RandomForestRegressor pred : ',rpred[:5])
print('RandomForestRegressor real : ',y[:5])
print('결정 계수 : ',r2_score(y, rpred))

print('XGBRegressor ----------------------')
xmodel = XGBRegressor(criterion='squared_error').fit(x,y)
xpred = xmodel.predict(x)
print('XGBRegressor pred : ',xpred[:5])
print('XGBRegressor real : ',y[:5])
print('결정 계수 : ',r2_score(y, xpred))

print('SVR ----------------------')
smodel = SVR().fit(x,y)
spred = smodel.predict(x)
print('SVR pred : ',spred[:5])
print('SVR real : ',y[:5])
print('결정 계수 : ',r2_score(y, spred))

print('KNeighborsRegressor ----------------------')
kmodel = KNeighborsRegressor().fit(x,y)
kpred = kmodel.predict(x)
print('KNeighborsRegressor pred : ',kpred[:5])
print('KNeighborsRegressor real : ',y[:5])
print('결정 계수 : ',r2_score(y, kpred))

