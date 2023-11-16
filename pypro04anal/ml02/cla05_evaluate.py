# 분류모델 성능 파악을 위해 Confusion matrix를 활용
# Accuracy, Precision, recall 등의 지표를 사용
# ROC curve, AUC 도 사용
# 연구 보고서 주제 설정 -> 데이터 수집 및 가공 -> 모델 생성 및 학습 -> 모델을 평가 -> 유의하다면 인사이트를 얻어 의사결정 자료로 활용

from sklearn.datasets import make_classification # 분류를 위해 sklearn에서 제공하는 데이터
from sklearn.linear_model import LogisticRegression 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

x, y = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=123)
# 표본, 독립변수, n_redundant 독립변수 중 다른 독립변수의 선형조합으로 나타낸 성분 수
print(x[:3], x.shape)
print(y[:3], y.shape)

# plt.scatter(x[:,0], x[:,1])
# plt.show()

model = LogisticRegression().fit(x, y)
y_hat = model.predict(x)
print('예측값  y_hat : ', y_hat[:3])
print()
# 판별 경계선 설정
f_value = model.decision_function(x) # 결정함수(판별함수) : 불확실성 추정함수. 판별 경계선 설정을 위한 샘플 데이터 지원
print('f_value : ',f_value[:10])    # 양수 값은 양성 클래스를 의미하며 음수 값은 음수 클래스를 의미
# f_value :  [-0.28578195 -0.94087863 -4.23244981  2.80427449  0.06138614
#                         0         0               0                    1           1

df = pd.DataFrame(np.vstack([f_value, y_hat, y]).T, columns=['f_value','y_hat','y'])
print(df.head(3))

from sklearn.metrics import confusion_matrix 
print(confusion_matrix(y, y_hat))
#             실제값
#             Y        n
# 예측값 y [[44(TP)  4(FN)]
#         n  [ 8(FP) 44(TN]]
acc = (44+44)/100 # TP+TN / 전체수
recall = 44/(44+4) # TP/TP+FN
precission = 44/(44+8) # TP / TP + FP
specificity =  44/(44+8) # TN / FP +TN
fallout = 8/(8+44) # FP/(FP+TN)
print('acc(정확도) : ',acc)
print('recall(재현율, 민감도, TPR) : ',recall)
print('precission(정밀도) : ', precission) # 전체 양성 자료 중에 양성으로 예측된 비율. 1에 가까울 수록 좋음
print('specificity(특이도) : ',specificity)
print('fallout(위양성율, FPR) : ', fallout) # 전체 음성 자료 중에 양성으로 잘못 예측된 비율. 0에 가까울 수록 좋음
print('fallout(위양성율) : ', 1-specificity) 

print()
from sklearn import metrics 
ac_sco = metrics.accuracy_score(y, y_hat) # 실제값, 예측값 -> 순서 제대로 줘야함
print('ac_sco : ', ac_sco)
cl_rep = metrics.classification_report(y, y_hat) # 전체 보기
print(cl_rep)

print()
fpr, tpr, threshold = metrics.roc_curve(y,  model.decision_function(x))
print('fpr : ',fpr)
print('tpr : ',tpr)
print('분류결정 임계값 : ', threshold)

# ROC(Receiver Operator Characteristic, 수신자 판단) Curve는 클래스 판별 기준값의 변화에 따른 Fall-out과 Recall의 변화를 시각화 함.
#  FPR이 변할 때 TPR이 어떻게 변화하는지를 나타내는 곡선이다.
# ROC는 위양성률(1-특이도)을 x축으로, 그에 대한 실제 양성률(민감도)을 y축 으로 놓고 그 좌푯값들을 이어 그래프로 표현한 것이다. 
# 일반적으로 0.7~0.8 수준이 보통의 성능을 의미한다. 0.8~0.9는 좋음, 0.9~1.0은 매우 좋은 성능을 보이는 모델이라 평가할 수 있다.

plt.plot(fpr, tpr, 'o-', label='LogisticRegression')
plt.plot([0,1],[0,1],'k--',label='Random classifier line(AUC:0.5)')
plt.plot([fallout],[recall], 'ro', ms=10)
plt.xlabel('fpr', fontdict={'fontsize':16})
plt.ylabel('tpr')
plt.legend()
plt.show()

# AUC(Area Under the ROC Curve)는 ROC curve의 밑면적을 말한다. 즉, 성능 평가에 있어서 수치적인 기준이 될 수 있는 값으로,
# 1에 가까울수록 그래프가 최상단에 근접하게 되므로 좋은 모델이라고 할 수 있다.
print('AUC : ',metrics.auc(fpr, tpr)) # AUC :  0.9547275641025641 -> 아주 좋은 모델