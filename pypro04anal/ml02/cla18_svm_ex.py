# [SVM 분류 문제] 심장병 환자 데이터를 사용하여 분류 정확도 분석 연습
# https://github.com/pykwon/python/tree/master/testdata_utf8         Heartcsv
#
# Heart 데이터는 흉부외과 환자 303명을 관찰한 데이터다. 
# 각 환자의 나이, 성별, 검진 정보 컬럼 13개와 마지막 AHD 칼럼에 각 환자들이 심장병이 있는지 여부가 기록되어 있다. 
# dataset에 대해 학습을 위한 train과 test로 구분하고 분류 모델을 만들어, 모델 객체를 호출할 경우 정확한 확률을 확인하시오. 
# 임의의 값을 넣어 분류 결과를 확인하시오.     
# 정확도가 예상보다 적게 나올 수 있음에 실망하지 말자. ㅎㅎ
#
# feature 칼럼 : 문자 데이터 칼럼은 제외
# label 칼럼 : AHD(중증 심장질환)
#
# 데이터 예)
# "","Age","Sex","ChestPain","RestBP","Chol","Fbs","RestECG","MaxHR","ExAng","Oldpeak","Slope","Ca","Thal","AHD"
# "1",63,1,"typical",145,233,1,2,150,0,2.3,3,0,"fixed","No"
# "2",67,1,"asymptomatic",160,286,0,2,108,1,1.5,2,3,"normal","Yes"

from sklearn import svm, metrics 
from sklearn.model_selection import train_test_split 
import matplotlib.pyplot as plt 
import pandas as pd 
from sklearn.preprocessing import StandardScaler

# 데이터 읽기
data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/Heart.csv')
print(data.head(3),data.shape) # (303, 15)
print(data.columns)

# 데이터 정제
print(data.isna().any())
print('Ca na : ',data['Ca'].isnull().sum()) # 4
print('Thal na : ',data['Thal'].isnull().sum()) # 2
data = data.dropna() # na인 행 적어서 그냥 제거해버림
print(data.shape)

# ChestPain
print(data.ChestPain, data.ChestPain.unique())
mapping = {'typical': 1, 'asymptomatic': 2, 'nonanginal': 3, 'nontypical':4}
data['ChestPain'] = data['ChestPain'].map(mapping)

# Thal
print(data.Thal, data.Thal.unique()) 
mapping = {'fixed': 1, 'normal': 2, 'reversable': 3, 'nan':4}
data['Thal'] = data['Thal'].map(mapping)

y = data['AHD']
x = data.drop(['AHD','Unnamed: 0'], axis=1)

# train / test split 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=158)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) 

model = svm.SVC().fit(x_train, y_train)
print(model)

pred = model.predict(x_test)
print('예측값 : ',pred[:10])
print('실제값 : ',y_test[:10].values)

ac_score = metrics.accuracy_score(y_test, pred)
print('정확도 : ',ac_score)

# 새로운 값으로 분류 예측
newdata = pd.DataFrame({
    'Age': [69, 59, 70],
    'Sex': [1, 0, 1],
    'ChestPain': ['typical', 'asymptomatic', 'nontypical'],
    'RestBP': [145, 120, 160],
    'Chol': [240, 250, 280],
    'Fbs': [1, 0, 0],
    'RestECG': [2, 2, 2],
    'MaxHR': [150, 108, 129],
    'ExAng': [0, 1, 1],
    'Oldpeak': [2.5, 1.5, 2.6],
    'Slope': [3, 2, 2],
    'Ca': [0.0, 3.0, 2.0],
    'Thal': ['normal', 'fixed', 'reversable']
})

# ChestPain, Thal을 매핑하여 숫자로 변환
mapping_cp = {'typical': 1, 'asymptomatic': 2, 'nonanginal': 3, 'nontypical': 4}
newdata['ChestPain'] = newdata['ChestPain'].map(mapping_cp)

mapping_thal = {'fixed': 1, 'normal': 2, 'reversable': 3, 'nan': 4}
newdata['Thal'] = newdata['Thal'].map(mapping_thal)


# 새로운 데이터의 열 이름과 순서를 모델을 학습할 때와 동일하게 조정
newdata = newdata[['Age', 'Sex', 'ChestPain', 'RestBP', 'Chol', 'Fbs', 'RestECG', 'MaxHR', 'ExAng', 'Oldpeak', 'Slope', 'Ca', 'Thal']]

# 예측
newPred = model.predict(newdata)
print('새로운 예측 결과 : ', newPred)



