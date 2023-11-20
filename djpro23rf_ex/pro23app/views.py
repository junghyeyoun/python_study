from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from django.utils.safestring import mark_safe
import matplotlib.pyplot as plt


# Create your views here.
def MainFunc(request):
    df,accuracy = TestFunc()
    return render(request, 'main.html', {'accuracy': accuracy, 'dataframe': df.head(3)})

def TestFunc():
    # 데이터 불러오기
    df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/patient.csv')
    
    # 결측치 유무 확인
    # print(df.isnull().any())
    
    '''
    # 'STA'를 예측하는 데 중요한 변수들을 확인하기 위해 데이터를 준비
    # 필요한 열 선택
    df_x = df[['AGE', 'SEX', 'RACE', 'SER', 'CAN', 'CRN', 'INF', 'CPR', 'HRA']]
    df_y = df['STA']

    # 학습 데이터와 테스트 데이터로 분리
    train_x, test_x, train_y, test_y = train_test_split(df_x, df_y, test_size=0.2, random_state=12)

    # 분류 모델 생성 (랜덤 포레스트 분류기)
    model = RandomForestClassifier(criterion='entropy', n_estimators=2000)
    model.fit(train_x, train_y)

    # 변수 중요도 확인
    print('특성(변수, feature) 중요도 : ', model.feature_importances_) 
    # [0.36093824 0.02311725 0.01619555 0.02949197 0.18371808 0.03678692 0.08715503 0.14905796 0.113539]
    # -> 'SEX', 'RACE', 'SER', 'CRN' 는 임계값 0.05보다 낮기 때문에 종속변수에 큰 영향을 주는 변수가 아님.
    
    # 특성 중요도 시각화
    def plot_feature_importances(model):
        n_features = df_x.shape[1]
        plt.barh(range(n_features), model.feature_importances_, align='center')
        plt.yticks(range(n_features), df_x.columns)
        plt.xlabel("attr importances")
        plt.ylabel("attr")
        plt.ylim(-1, n_features)
        plt.savefig('C:/work/pysou/djpro23rf_ex/pro23app/static/images/feature_importances.png') # 그림을 파일로 저장
            
    plot_feature_importances(model)  # 특성 중요도 시각화 함수 호출하여 실행
    '''
    
    # 필요한 열 선택
    df_x = df[['AGE', 'INF', 'CAN', 'CPR', 'HRA']]
    df_y = df['STA']
    
    # 학습 데이터와 테스트 데이터로 분리
    train_x, test_x, train_y, test_y = train_test_split(df_x, df_y, test_size=0.2, random_state=12)

    # 분류 모델 생성 (랜덤 포레스트 분류)
    model = RandomForestClassifier(criterion='entropy', n_estimators=500)
    model.fit(train_x, train_y)

    # 모델 평가 (정확도 계산)
    pred = model.predict(test_x)
    accuracy = accuracy_score(test_y, pred)
    
    return df, accuracy

def ShowFunc(request):
    return render(request, 'show.html')

def ListFunc(request):
    if request.method == 'POST':
        # 사용자로부터 POST 요청을 받아서 데이터 추출
        age = int(request.POST['age'])
        sex = int(request.POST['sex'])
        race = int(request.POST['race'])
        ser = int(request.POST['ser'])
        can = int(request.POST['can'])
        crn = int(request.POST['crn'])
        inf = int(request.POST['inf'])
        cpr = int(request.POST['cpr'])
        hra = int(request.POST['hra'])

        # 기존 데이터셋을 읽어와 모델을 학습
        df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/patient.csv')
        x = df[['AGE', 'INF', 'CAN', 'CPR', 'HRA']]  # 종속 변수에 주요 영향을 주는 변수
        y = df['STA']  # 종속 변수

        model = RandomForestClassifier(criterion='entropy', n_estimators=500)
        model.fit(x, y)

        # 사용자 입력으로 예측
        user_input = [[age,inf,can, cpr, hra]]  # 모델 예측을 위한 입력 데이터
        prediction = model.predict(user_input)

        # 데이터 전송
        prediction_str = f" {prediction[0]} <br> {'생존' if prediction[0] == 0 else '사망'}"
        prediction_str_safe = mark_safe(prediction_str)
        
        return render(request, 'list.html', {'prediction': prediction_str_safe})
    return render(request, 'list.html', {'prediction': None})
