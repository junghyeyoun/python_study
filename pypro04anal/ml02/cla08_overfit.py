# 과적합 방지 목적으로 : train/test split, KFold, GridSearch ...
from sklearn.datasets import load_iris 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score 

iris = load_iris()
print(iris.keys())

train_data = iris.data 
train_label = iris.target
print(train_data[:2])
print(train_label[:2])

# 분류 모델
dt_clf = DecisionTreeClassifier() # 다른 모델도 가능
dt_clf.fit(train_data, train_label)
pred = dt_clf.predict(train_data)
print('예측값 : ',pred[:10])
print('실제값 : ',train_label[:10])
print('분류 정확도 : ', accuracy_score(train_label, pred)) # 1.0 -> 과적합 의심

print('\n 과적합 방지 방법1 : train/test split')
from sklearn.model_selection import train_test_split 

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=121)
dt_clf.fit(x_train, y_train)    # train으로 학습
pred2 = dt_clf.predict(x_test) # test로 검증
print('예측값 : ',pred2[:10])
print('실제값 : ',y_test[:10])
print('분류 정확도 : ', accuracy_score(y_test, pred2)) # 0.9555555555555556 포용성이 있는 모델 생성

print('\n과적합 방지 방법 2 : 교차검증(cross validation, kFold)')
from sklearn.model_selection import KFold
import numpy as np
feature = iris.data
label = iris.target
dt_clf = DecisionTreeClassifier(random_state=123)
kfold = KFold(n_splits=5)  # kfold 5개로 나눠
cv_acc = []  # 리스트 형태로 담을거임. 5개의 acc를
print('iris shape : ', feature.shape)  #  (150, 4)
# 전체 행 수가 150, 학습데이터 0.8 * 150 = 120, 검증데이터 30

n_iter = 0
for train_index, test_index in kfold.split(feature):
    # print('n_iter : ',n_iter)
    # print(train_index, ' ',train_index)
    # print(test_index,' ',test_index)
    xtrain, xtest = feature[train_index], feature[test_index]
    ytrain, ytest = label[train_index], label[test_index]
    
    # 모델 생성중 학습 및 예측
    dt_clf.fit(xtrain, ytrain) # 학습
    pred = dt_clf.predict(xtest) # 검증
    n_iter += 1
    
    # 반족할 때 마다 정확도 측정
    acc = np.round(accuracy_score(ytest, pred), 3)
    train_size = xtrain.shape[0]
    test_size = xtest.shape[0]
    print('반복수:{0}, 교차검증 정확도:{1}, 학습데이터 크기:{2}, 검증데이터 크기:{3}'.format(n_iter, acc, train_size, test_size))
    print('반복수:{0}, 검증 자료 인덱스:{1}'.format(n_iter, test_index))
    
    cv_acc.append(acc)
    
print('모델 생성 도중 평균 검증 정확도 : ', np.mean(cv_acc)) # 0.9199999999999999

print('\n실제로 교차검증(cross vaildation, KFold) 시 cross_val_score 사용')
from sklearn.model_selection import cross_val_score # sklearn이 KFold를 내부적으로 지원
data = iris.data 
label = iris.target 

score = cross_val_score(dt_clf, data, label, scoring='accuracy', cv=5)
print('교차 검증별 정확도 : ',np.round(score, 3))
print('모델 생성 도중 평균 검증 정확도 : ', np.round(np.mean(score),3)) # 0.96

# StratifiedKFold : 불균형한 분포를 가진 레이블 데이터인 경우 사용. ex) 대출사기 - 대부분 정상, 극히 일부 사기
from sklearn.model_selection import StratifiedKFold 
# ...

print('\n과적합 방지 방법 3 : GridSearchCV')
from sklearn.model_selection import GridSearchCV