# [로지스틱 분류분석 문제3]
# Kaggle.com의 https://www.kaggle.com/truesight/advertisingcsv  file을 사용
# 얘를 사용해도 됨   'testdata/advertisement.csv' 
# 참여 칼럼 : 
#   Daily Time Spent on Site : 사이트 이용 시간 (분)
#   Age : 나이,
#   Area Income : 지역 소독,
#   Daily Internet Usage:일별 인터넷 사용량(분),
#   Clicked Ad : 광고 클릭 여부 ( 0 : 클릭x , 1 : 클릭o )
# 광고를 클릭('Clicked on Ad')할 가능성이 높은 사용자 분류.
# 데이터 간의 단위가 큰 경우 표준화 작업을 시도한다.
# ROC 커브와 AUC 출력

from sklearn.datasets import make_classification 
from sklearn.linear_model import LogisticRegression 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score 

df = pd.read_csv('../testdata/advertisement.csv')
print(df.head(3), df.shape)
print(df.columns)

# train / test split
x = df[['Daily Time Spent on Site', 'Age','Area Income', 'Daily Internet Usage']]
y = df['Clicked on Ad']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0, shuffle=True)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) 

# 정규화
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(x_train)
sc.fit(x_test)
x_train = sc.transform(x_train)
x_test = sc.transform(x_test)
print(x_train[:3])
# 정규화 하기전 분류 정확도 : 0.91667
# 정규화 한 후 분류 정확도 : 0.96667

# 모델 작성
model = LogisticRegression(C=1.0, solver='lbfgs', multi_class='auto', random_state=0, verbose=0)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print('예측값 : ', y_pred[:10])
print('실제값 : ', y_test.values[:10])
print('총 갯수 : %d, 오류 수 : %d'%(len(y_test), (y_test != y_pred).sum()))

print('\n분류 정확도 확인')
print('%.5f'%accuracy_score(y_test, y_pred)) 

# confusion matrix의 값들 보기
from sklearn import metrics 
cl_rep = metrics.classification_report(y_test, y_pred) 
print(cl_rep)

# ROC 곡선
fpr, tpr, threshold = metrics.roc_curve(y,  model.decision_function(x))
plt.plot(fpr, tpr, 'o-', label='LogisticRegression')
plt.plot([0,1],[0,1],'k--',label='Random classifier line(AUC:0.5)')
plt.xlabel('fpr', fontdict={'fontsize':16})
plt.ylabel('tpr')
plt.legend()
plt.show()

# AUC
print('AUC : ',metrics.auc(fpr, tpr)) # AUC :  0.7726159999999999