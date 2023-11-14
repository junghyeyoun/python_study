from django.shortcuts import render
from proapp.models import Jikwon
from sklearn.linear_model import LinearRegression 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, explained_variance_score, mean_squared_error 
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
import pandas as pd
from sklearn.model_selection import train_test_split
from django.db.models import F
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse, JsonResponse

# Create your views here.
def Main(request):
    return render(request, "main.html") 

@csrf_exempt  
def Go(request):
    # 데이터 불러오기 및 정제
    year = Jikwon.objects.annotate(근무년수=now().year - F('jikwon_ibsail__year'))
    datas = year.values('jikwon_no', 'jikwon_name', 'buser_num__buser_name', 'jikwon_jik', 'jikwon_pay', '근무년수')
    #print(datas)
    df = pd.DataFrame(datas)
    df.columns = ['사번', '직원명', '부서명', '직급', '연봉', '근무년수']
    #print(df)
    
    # dataset 분리
    train, test = train_test_split(df, test_size=0.4)
    x_train = train[['근무년수']]
    y_train = train['연봉'] 
    x_test = test[['근무년수']]
    y_test = test['연봉']
    #print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
    
    # LinearRegression
    model = LinearRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    print('실제값 : ',y_test.values)
    print('예측값 : ',np.round(y_pred))
    
    # 결정계수
    r2 = r2_score(y_test, y_pred)
    r2 = round(r2 * 100) 
    
    new_year = request.POST.get('yearsOfWork')
    
    if new_year is not None:  
        new_year = float(new_year)  
        new_pred = model.predict([[new_year]])  
        predicted_salary = round(new_pred[0]) 
        print('%s 년 근무 했을 경우 예상 연봉은 %s입니다.' % (new_year, new_pred[0]))
    else:
        print('근무 년수를 입력하세요.')
    
    jk_payavg = df.pivot_table(index='직급', values='연봉', aggfunc=np.mean)
    jk_payavg_dict = jk_payavg.to_dict()['연봉']
    print('직급별 연봉 평균\n', jk_payavg, '\n')

    return JsonResponse({'predicted_salary': predicted_salary, 'r2': r2, 'jk_payavg': jk_payavg_dict})
