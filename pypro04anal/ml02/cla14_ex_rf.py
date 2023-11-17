# [Randomforest 문제1] 
# kaggle.com이 제공하는 'Red Wine quality' 분류 ( 0 - 10)
# dataset은 winequality-red.csv 
# https://www.kaggle.com/sh6147782/winequalityred?select=winequality-red.csv
# Input variables (based on physicochemical tests):
#  1 - fixed acidity
#  2 - volatile acidity
#  3 - citric acid
#  4 - residual sugar
#  5 - chlorides
#  6 - free sulfur dioxide
#  7 - total sulfur dioxide
#  8 - density
#  9 - pH
#  10 - sulphates
#  11 - alcohol
#  Output variable (based on sensory data):
#  12 - quality (score between 0 and 10)

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split 
import pandas as pd 
import numpy as np

wine = pd.read_csv('../testdata/winequality-red.csv')
print(wine.head(2),wine.shape) # (1596, 12)
print(wine.isnull().any()) # 결측치 없음

x = wine.drop('quality', axis=1)
y = wine['quality']
print(x.head(2),x.shape, x.columns)
print(y.head(2),y.shape)

# train / test split
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2, random_state=12)

# model
model = RandomForestClassifier(criterion='entropy',n_estimators=500) 
model.fit(train_x, train_y)

# 중요 변수(feature) 확인
print('특성(변수, feature) 중요도 : ',model.feature_importances_) # [0.15706537 0.54155886 0.30137578]
import matplotlib.pyplot as plt 

def plot_feature_important_func(model):
    n_features = x.shape[1]
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features),x.columns)
    plt.xlabel('importance')
    plt.ylabel('feature name')
    plt.show()
    
plot_feature_important_func(model)

# 교차 검증 (KFold) 
from sklearn.model_selection import cross_val_score
cross_vali = cross_val_score(model, x, y, cv=5)
print(cross_vali)
import numpy as np 
print('교차검증  5회 진행 정확도 평균 : ',np.round(np.mean(cross_vali),3))

# 모델 검정
pred = model.predict(test_x)
print('예측값 : ',pred[:5])
print('실제값 : ',test_y[:5].ravel()) 
from sklearn.metrics import accuracy_score 
print('acc : ',accuracy_score(test_y, pred))

