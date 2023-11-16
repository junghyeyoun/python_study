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

print('-------------------------------------------------------------------------------------------------------')
print('\n 다른 문제 풀이')
url = 'https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/bodycheck.csv'
df = pd.read_csv(url)
print(df.head(3), df.shape)  # (20, 6)
print()

# train / test split(7:3)
x = df[['게임', 'TV시청']]
y = df['안경유무']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0, shuffle=True)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)  # (14, 2) (6, 2) (14,) (6,)

# 모델작성
model = LogisticRegression(C=0.000055, solver='lbfgs', multi_class='auto', random_state=0, verbose=0)
model.fit(x_train, y_train)

# 분류 예측
y_pred = model.predict(x_test)
print('예측값 : ', y_pred)
print('실제값 : ', y_test.values)
print('총 갯수 : %d, 오류 수 : %d'%(len(y_test), (y_test != y_pred).sum()))

print('\n분류 정확도 확인 1')
print('%.5f'%accuracy_score(y_test, y_pred))  # 0.66667

print('\n분류 정확도 확인 2')
con_mat = pd.crosstab(y_test, y_pred, rownames=['예측값'], colnames=['관측값'])
print(con_mat)
print((con_mat[0][0] + con_mat[1][1]) / len(y_test))  # 0.6666

print('\n분류 정확도 확인 3')
print('test로 정확도는 ', model.score(x_test, y_test))  # 0.666
print('train으로 정확도는 ', model.score(x_train, y_train))  # 0.5714


print('새로운 값으로 분류 예측')
print(x_test[:2])
a = int(input('게임 이용 시간을 양의 정수로 입력하시오 : '))
b = int(input('TV  시청 시간을 양의 정수로 입력하시오 : '))
new_data = np.array(([[a,b]]))
new_pred = model.predict(new_data)
result = ('안경쓸듯' if new_pred == 1 else '안경 안 쓸듯')

print('예측 결과 : ', result)
# print('softmax 결과(날것) : ', model.predict_proba(new_data))