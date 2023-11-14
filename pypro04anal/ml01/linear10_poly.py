# 비선형 회귀분석(Non-linear regression) - 다항회귀분석
# 데이터가 곡선의 형태로 분포되어 있는 경우에 직선의 회귀식(잔차가 큼)을 곡선으로 변환해(잔차가 작음) 보다 더 정확하게 데이터 변화를 예측하는데 그 목적이 있다.

# 입력자료 특징/특성(독립변수, feature) 변환으로 선형모델 개선
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = np.array((1,2,3,4,5))
y = np.array((4,2,1,3,7))

# plt.scatter(x, y)
# plt.show()

print(np.corrcoef(x,y)) # 0.48076197 의미없다. -> 데이터의 분포가  곡선의 형태이기 때문

# 선형회귀모델 작성 
from sklearn.linear_model import LinearRegression 
# 차원 확대하기 전 오류
# Expected 2D array, got 1D array instead -> reshape을 써도 괜찮음
x = x[:, np.newaxis] # 차원 확대
print(x)
model = LinearRegression().fit(x, y) 
ypred = model.predict(x)
print('ypred : ',ypred)

# plt.scatter(x, y)
# plt.plot(x, ypred, c='red')
# plt.show()
#
# print('r2_score : ', r2_score(y, ypred))

# feature에 항(다항식 특징)을 추가 
from sklearn.preprocessing import PolynomialFeatures 

poly = PolynomialFeatures(degree=2, include_bias=False)
x2 = poly.fit_transform(x) # 특징행렬을 생성. x를 나타낸 값, x**2 값 (degree에 따라 달라짐)
print(x2)

model2 = LinearRegression().fit(x2, y) 
ypred2 = model2.predict(x2)
print('ypred2 : ',ypred2)

plt.scatter(x, y)
plt.plot(x, ypred2, c='blue')
plt.show()

print('r2_score : ', r2_score(y, ypred2))

