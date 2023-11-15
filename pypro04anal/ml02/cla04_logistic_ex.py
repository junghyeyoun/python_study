# [로지스틱 분류분석 문제2] 
# 게임, TV 시청 데이터로 안경 착용 유무를 분류하시오.
# 안경 : 값0(착용X), 값1(착용O)
# 예제 파일 : https://github.com/pykwon  ==>  bodycheck.csv
# 새로운 데이터(키보드로 입력)로 분류 확인. 스케일링X

from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False

from sklearn.linear_model import LogisticRegression 

data = pd.read_csv('../testdata/bodycheck.csv')
# 게임, TV만 추출
data = data[['게임', 'TV시청','안경유무']]
print(data,type(data))

x = data[['게임','TV시청']]
y = data[['안경유무']]
# print(x)
# print(y)

# train / test split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=2, shuffle=True)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)


# 모델 작성 -------------------------------
model = LogisticRegression(C=1.0, solver='lbfgs', multi_class='auto', verbose=1)
print(model)
# ---------------------------------------

model.fit(x_train, y_train)

# 분류 예측
a = int(input('게임시간 입력: '))
b = int(input('TV 시청시간 입력: '))
input_data = np.array([[a, b]])  
new_pred = model.predict(input_data)
print('예측값 : ', new_pred)

print('분류 정확도 확인')
y_pred = model.predict(x_test)
print('%.5f'%accuracy_score(y_test, y_pred))
print('총 개수 : %d, 오류수 : %d'%(len(y_test),(y_test.values.ravel() != y_pred).sum())) 
# ravel() -> 차원축소