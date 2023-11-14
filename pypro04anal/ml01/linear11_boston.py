# Boston Housing Price (보스턴 주택 가격 데이터)로 선형회귀 모델 생성

import numpy as np 
import pandas as pd 
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt 
plt.rc('font', family='malgun gothic')
df = pd.read_csv('../testdata/housing.data',header=None, sep='\s+')
df.columns = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']
print(df.head(2), df.shape)
print(df.corr()) # MEDV(본인 소유 주택 가격), LSTAT(하위계층 비율) : -0.737663

x = df[['LSTAT']].values
y = df['MEDV'].values
model = LinearRegression()
model.fit(x, y)

# 다항 특성
quad = PolynomialFeatures(degree=2)
x_quad = quad.fit_transform(x)
print(x_quad)
# [[ 1.      4.98   24.8004]
#  [ 1.      9.14   83.5396]
#  [ 1.      4.03   16.2409]
#  ...

cubic = PolynomialFeatures(degree=3)
x_cubic = cubic.fit_transform(x)
print(x_cubic)
# [[  1.         4.98      24.8004   123.505992]
# [  1.         9.14      83.5396   763.551944]
# [  1.         4.03      16.2409    65.450827]


# y_lin_fit = model.predict(x)
# model_r2 = r2_score(y, y_lin_fit)
# print('model_r2 : ', model_r2) # 0.5441462

# 차트 작성용 시작
x_fit = np.arange(x.min(), x.max(), 1)[:,np.newaxis] 
print(x_fit)
# [[ 1.73]
#  [ 2.73]
#  [ 3.73]
#  ... ]]

# degree =1
model.fit(x, y)
y_lin_fit = model.predict(x_fit)
# 차트 작성용 끝
model_r2 = r2_score(y, model.predict(x))
print('model_r2 : ', model_r2)

# degree =2 
model.fit(x_quad, y)
y_quad_fit = model.predict(quad.fit_transform(x_fit)) 
# 차트 작성용 끝 
quad_r2 = r2_score(y, model.predict(x_quad))
print('quad_r2 : ', quad_r2)

# degree =3 
model.fit(x_cubic, y)
y_cubic_fit = model.predict(cubic.fit_transform(x_fit)) 
# 차트 작성용 끝 
cubic_r2 = r2_score(y, model.predict(x_cubic))
print('cubic_r2 : ', cubic_r2)

# 시각화
plt.scatter(x, y, label='traning data', c='lightgray')

plt.plot(x_fit, y_lin_fit, linestyle=':', label='linear fit(d = 1), $R^2=%.2f$'%model_r2, c = 'b', lw=3)
plt.plot(x_fit, y_quad_fit, linestyle='-', label='quad fit(d = 2), $R^2=%.2f$'%quad_r2, c = 'r', lw=3)
plt.plot(x_fit, y_cubic_fit, linestyle='--', label='cubic fit(d = 3), $R^2=%.2f$'%cubic_r2, c = 'g', lw=3)
plt.xlabel('하위계층비율')
plt.ylabel('주택가격')
plt.legend()
plt.show()

