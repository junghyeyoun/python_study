# SVM : 데이터 분류 및 예측을 위한 가장 큰 폭의 경계선을 찾은 알고리즘을 사용.
# 커널트릭이라는 기술을 통해 선형은 물론 비선형, 이미지 분류 까지도 처리 가능

# SVM으로 xor 처리를 실습
x_data = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]

import pandas as pd 
import numpy as np 
from sklearn.linear_model import LogisticRegression 
from sklearn import svm, metrics 

df = pd.DataFrame(x_data)
print(df) 

feature = np.array(df.iloc[:,0:2])
label = np.array(df.iloc[:,2])
print(feature)
print(label)

model1 = LogisticRegression().fit(feature, label)  
pred = model1.predict(feature)
print('Logistic 예측값 : ',pred)
print('Logistic acc : ',metrics.accuracy_score(label, pred))
print()

model2 = svm.SVC(C=1.0).fit(feature, label)   # C : 과적합 방지. 패널티 주기
#model2 = svm.LinearSVC().fit(feature, label)  # 선형인 경우에
pred2 = model2.predict(feature)  # 예측
print('SVM 예측값 : ',pred2)
print('SVM acc : ',metrics.accuracy_score(label, pred2))
print()
