# [GaussanNB 문제] 
# 독버섯(poisonous)인지 식용버섯(edible)인지 분류
# https://www.kaggle.com/datasets/uciml/mushroom-classification
# feature는 중요변수를 찾아 선택, label:class
# 참고 : from xgboost import plot_importance
# 데이터 변수 설명 : 총 23개 변수가 사용됨.
# 여기서 종속변수(반응변수)는 class 이고 나머지 22개는 모두 입력변수(설명변수, 예측변수, 독립변수).
# 변수명 변수 설명

import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.naive_bayes import GaussianNB, MultinomialNB 
from sklearn.metrics import accuracy_score, classification_report 
import numpy as np 
from xgboost import plot_importance
import matplotlib.pyplot as plt
import xgboost as xgb

df = pd.read_csv('../testdata/mushrooms.csv')
print(df.head(3), df.shape)
print(df.columns)

feature = df.drop(['class'], axis=1)
print(feature.head(5))

label = df['class'] #.map({'p':1, 'e':0})
print(label.head(5), label.unique())

from sklearn.preprocessing import LabelEncoder

# label 숫자로 변환
label_encoder = LabelEncoder()
label = label_encoder.fit_transform(df['class'])

# 나머지 문자열 칼럼들을 변환
for column in feature.columns:
    feature[column] = label_encoder.fit_transform(feature[column])
    
# print(label)
# print(feature)

# train/test split
train_x, test_x, train_y, test_y = train_test_split(feature, label, random_state=0, test_size=0.2 )
print(train_x.shape, test_x.shape, train_y.shape, test_y.shape)

# model
gmodel = GaussianNB()
print(gmodel)
gmodel.fit(train_x, train_y)

# 피쳐 중요도 시각화
model = xgb.XGBClassifier() # 피쳐 중요도를 위해 xgboost모델 생성
model.fit(train_x, train_y)
plot_importance(model)
plt.show()

pred = gmodel.predict(test_x)
print('예측값 : ',pred[:10])
print('실제값 : ',test_y[:10])

acc = sum(test_y == pred) / len(pred)
print('정확도 : ',acc)
print('정확도 : ',accuracy_score(test_y, pred))
print('분류 보고서 : \n', classification_report(test_y, pred))

# ****************************************************************************************
print('다른 문제 풀이')

from xgboost import XGBClassifier

df = pd.read_csv('../testdata/mushrooms.csv')

# class를 제외한 독립변수 선택
features = df.drop('class', axis=1)
features = pd.get_dummies(features)
label = df['class'].map({'p':1, 'e':0})


# 학습 및 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=12)

# XGBClassifier 모델 생성 및 학습
model = XGBClassifier()
model.fit(X_train, y_train)

# 특성 중요도 시각화
plot_importance(model)
plt.show()
print(df.columns)

features2 = features[['gill-size_b', 'odor_n', 'bruises_f']].copy()


# 학습 및 테스트 데이터 분리
train_x, test_x, train_y, test_y = train_test_split(features2, label, test_size=0.2, random_state=6413)

# GaussianNB 모델 생성 및 학습
gmodel = GaussianNB()
gmodel.fit(train_x, train_y)

# 예측
pred = gmodel.predict(test_x)
print('예측값 : ', pred[:10])
print('실제값 : ', test_y[:10])

# 정확도 평가
acc = sum(test_y == pred) / len(pred)
print('정확도 : ', acc) # 0.9415
print('정확도 : ', accuracy_score(test_y, pred)) # 0.9415
print('분류 보고서 : \n', classification_report(test_y, pred))

