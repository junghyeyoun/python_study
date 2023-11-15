# 인디언들의 당뇨병 관련 데이터를 이용해 이항분류 : logisticRegression 클래스 사용
# Pregnancies : 임신 횟수
# Glucose: 포도당 부하 검사 수치
# BloodPressure: 혈압(mm Hg)
# SkinThickness: 팔 삼두근 뒤쪽의 피하지방 측정값(mm)
# Insulin: 혈청 인슐린(mu U/ml)
# BMI: 체질량지수(체중(kg)/키(m))^2
# DiabetesPedigreeFunction: 당뇨 내력 가중치 값
# Age: 나이
# Outcome: 클래스 결정 값(0 또는 1)
import pandas as pd 
from sklearn.model_selection  import train_test_split
from sklearn.linear_model import LogisticRegression # sigmoid 함수가 아니라 softmax 함수를 사용해 다항 분류가 가능
from sklearn.metrics import accuracy_score 

names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
df = pd.read_csv('../testdata/pima-indians-diabetes.data.csv', header=None, names = names)

print(df.head(3))
array = df.values
print(array[:3], array.shape) # (768, 9) -> matrix
x = array[:, 0:8]
y = array[:, 8]
print(x[:2], x.shape) # (768, 8) -> matrix
print(y[:2], y.shape) # (768,) -> vector

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=7)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
"""
model = LogisticRegression()
model.fit(x_train, y_train)
print('예측값 : ',model.predict(x_test[:10]))
print('실제값 : ',y_test[:10])
print((model.predict(x_test) != y_test).sum()) # 예측 실패 : 58
print('test로 검정한 분류 정확도 : ', model.score(x_test, y_test))  # test로 정확도 확인 -> 0.7489
print('train로 검정한 분류 정확도 : ', model.score(x_train, y_train))  # train으로 정확도 확인 -> 0.7839 
# -> test, train이 너무 다르게 나오면 과적합이다. 두 데이터의 분포가 너무 다르기 때문에 shuffle을 잘하고 split해줘야한다.
pred = model.predict(x_test)
print('분류 정확도 : ',accuracy_score(y_test, pred))
"""
# 모델을 만들었기 때문에 위의 코드 없어도 됨

# 모델 저장
import joblib 
#joblib.dump(model, 'cla03.model.sav') # 모델 저장 경로 

# 학습이 끝난 모델 파일 로딩 후 사용
mymodel = joblib.load('cla03.model.sav')
print(x_test[:1])
print('분류 예측 : ', mymodel.predict(x_test[:1])) # 분류 예측 : [0.] -> 당뇨병없는걸로 판단
