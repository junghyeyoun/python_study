# [XGBoost 문제] 
# kaggle.com이 제공하는 'glass datasets'          testdata 폴더 : glass.csv
# 유리 식별 데이터베이스로 여러 가지 특징들에 의해 7 가지의 label(Type)로 분리된다.
# RI    Na    Mg    Al    Si    K    Ca    Ba    Fe    
#  Type
#                        ...
# glass.csv 파일을 읽어 분류 작업을 수행하시오.

import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split 
import matplotlib.pyplot as plt 
from sklearn import metrics

import xgboost  
from xgboost import plot_importance 

glass = pd.read_csv('../testdata/glass.csv')
print(glass.head(3))
print(glass.isnull().any()) # na 없음

x = glass.drop('Type', axis=1)
y = glass['Type']
print(x.head(2),x.shape, x.columns)
print(y.head(2),y.shape)

# test/ train split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=12)

# model
model = xgboost.XGBClassifier(booster='gbtree', max_depth=6, n_estimators=500).fit(x_train, y_train)
print(model)

# model 검정
pred = model.predict(x_test)
print('예측값 : ',pred[:10])
print('예측값 : ',y_test[:10])

# 정확도
acc = metrics.accuracy_score(y_test,pred)
print('정확도 : ',acc) 
print(metrics.classification_report(y_test,pred))

# 
fig, ax = plt.subplots(figsize=(10,20))
plot_importance(model, ax=ax)
plt.show()