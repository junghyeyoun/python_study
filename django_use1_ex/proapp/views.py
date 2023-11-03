from django.db.models import F
from django.shortcuts import render
from django.utils.timezone import now
from proapp.models import Jikwon
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False  # 한글 처리때 음수가 깨지는 것을 방지하기 위해 사용


# Create your views here.
def mainFunc(request):
    # 1번
    year = Jikwon.objects.annotate(근무년수=now().year - F('jikwon_ibsail__year')).order_by('buser_num', 'jikwon_name')

    datas = year.values('jikwon_no', 'jikwon_name', 'buser_num__buser_name', 'jikwon_jik', 'jikwon_pay', '근무년수')
   # print(datas)
    df = pd.DataFrame(datas)
    df.columns = ['사번', '직원명', '부서명', '직급', '연봉', '근무년수']
    print(df)
    
    # 2번
    print()
    bn_paysum = df.pivot_table(index='부서명', values='연봉', aggfunc=sum)
    bn_payavg = df.pivot_table(index='부서명', values='연봉', aggfunc=np.mean)
    jk_paysum = df.pivot_table(index='직급', values='연봉', aggfunc=sum)
    jk_payavg = df.pivot_table(index='직급', values='연봉', aggfunc=np.mean)
    bn_payavg = bn_payavg.round(2)
    jk_payavg = jk_payavg.round(2)

    print('부서별 연봉 합\n',bn_paysum,'\n')
    print('부서별 연봉 평균\n',bn_payavg,'\n')
    print('직급별 연봉 합\n',jk_paysum,'\n')
    print('직급별 연봉 평균\n',jk_payavg,'\n')

    # 4번
    data = Jikwon.objects.values('jikwon_gen', 'jikwon_jik')
    df2 = pd.DataFrame(data)
    df2.columns = ['성별','직급']
    cross_tab = pd.crosstab(df2['성별'], df2['직급'], margins=True)
    print(cross_tab)
    
    # 3번
    df3 = df['연봉'].groupby(df['부서명'])
    df3 = {'sum': df3.sum(), 'avg': df3.mean()}
    
    rs = pd.DataFrame(df3)
    
    plt.figure(figsize=(10, 6))
    rs.plot.bar(rot=0)
    plt.title("부서별 급여 합/평균")
    plt.xlabel("부서명")
    plt.ylabel("급여")
    plt.legend(["급여 합", "급여 평균"])

    plt.savefig('django_use1_ex/proapp/static/images/buser_salary.png')
    
    
    return render(request, 'a.html',{'df':df.to_html(),'cross':cross_tab.to_html(),'bn_paysum':bn_paysum.to_html,
                                     'bn_payavg':bn_payavg.to_html,'jk_paysum':jk_paysum.to_html,'jk_payavg':jk_payavg.to_html,
                                     })
