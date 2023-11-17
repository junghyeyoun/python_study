# Ensemble 학습 : 개별적으로 동작하는 여러 모델들을 종합하여 예측한 결과를 투표에 의 가장 좋은 결과로 취하는 방법
# 

import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier

cancerData = load_breast_cancer()
dataDf = pd.DataFrame(cancerData.data, columns=cancerData.feature_names)
print(dataDf.head(3), dataDf.shape) # (569, 30)
print(set(cancerData.target)) # {0, 1} -> 이항분류
print(cancerData.target_names) # ['malignant'(0, 양성) 'benign'(1, 음성)]

x_train, x_test, y_train, y_test = train_test_split(cancerData.data, cancerData.target, test_size=0.2, random_state=12)

logiModel = LogisticRegression()
knnModel = KNeighborsClassifier(n_neighbors = 3)
decModel = DecisionTreeClassifier()

classifiers = [logiModel, knnModel, decModel]

for cl in classifiers:
    cl.fit(x_train, y_train)
    pred = cl.predict(x_test)
    class_name = cl.__class__.__name__ 
    print('{0}정확도는 : {1:.4f}'.format(class_name, accuracy_score(y_test, pred)))
    
voringModel = VotingClassifier(estimators=[('LR',logiModel),('KNN',knnModel),('Decision',decModel)], voting='soft')
voringModel.fit(x_train, y_train)

vpred = voringModel.predict(x_test)
print('보팅 분류의 정확도 : {0:.4f}'.format(accuracy_score(y_test, vpred)))