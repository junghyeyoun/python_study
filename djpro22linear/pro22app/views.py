from django.shortcuts import render
from django.http.response import JsonResponse
from pro22app.models import Jikwon
import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import joblib
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
model_created = False

def mainFunc(request):
    global model_created
    
    # if 문을 이용하여 모델을 한번만 만들고 계속 사용
    if not model_created:
        makeModel()
        model_created = True
        
    return render(request, 'index.html')

def makeModel():
    # jikwon 테이블에서 근무년수에 대한 연봉을 이용하여 회귀분석 모델을 작성
    datas = Jikwon.objects.values('jikwon_ibsail', 'jikwon_pay', 'jikwon_jik').all()
    df = pd.DataFrame.from_records(datas)
    # print(df.head(3), len(df))
    
    # 근무년수 구하기
    for i in range(len(df['jikwon_ibsail'])):
        df['jikwon_ibsail'][i] = int((datetime.now().date() - df['jikwon_ibsail'][i]).days/365)
    
    df.columns = ['근무년수', '연봉', '직급']
    # print(df.head(3))
    
    # train / test split (8:2)
    train, test = train_test_split(df, test_size=0.2, random_state=12)
    print(train.shape, test.shape)  # (24, 3) (6, 3)

    model_lm = LinearRegression().fit(X=train.iloc[:,[0]], y=train.iloc[:,[1]])
    
    # 성능 확인
    test_pred = model_lm.predict(test.iloc[:,[0]])
    print('연봉 예측값 :', test_pred[:5].flatten())
    print('연봉 실제값 :', test.iloc[:,[1]][:5].values.flatten())
    '''
    연봉 예측값 : [6827.05696203 4767.56329114 5282.43670886 3737.8164557  7341.93037975]
    연봉 실제값 : [7800 6600 5500 4000 8800]
    '''
    
    global r2
    r2 = r2_score(test.iloc[:,[1]], test_pred) * 100
    print('결정계수(설명력) :', r2, '%')
    # 결정계수(설명력) : 0.5523021663542762
    
    # 모델 저장
    joblib.dump(model_lm, 'djpro22linear/pro22app/static/model')  # 저장 경로
    
    # 직급별 연봉 평균
    global pay_jik
    pay_jik = df.groupby('직급').mean().round(1)
    print('pay_jik :', pay_jik)
    
@csrf_exempt   # csrf token을 적용하지 않음
def predFunc(request):
    year = request.POST.get('year')
    # print('year :', year)
    new_year = pd.DataFrame({'근무년수':[year]})
    
    # 모델 읽기 => 연봉을 예측하여 전송
    model = joblib.load('djpro22linear/pro22app/static/model')
    
    new_pred = round(model.predict(new_year)[0][0], 2)
    # print('new_pred : ', new_pred)
    
    return JsonResponse({'new_pred':new_pred, 'r2':r2, 'pay_jik':pay_jik.to_html()})

