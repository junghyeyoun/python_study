from django.shortcuts import render
from proexam3.models import Jikwon
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.rc('font', family='malgun gothic')
plt.rcParams['axes.unicode_minus'] = False

# Create your views here.
def Login(request):
    return  render(request, 'login.html')

def Gogo(request):
    jikwon_no = request.POST.get('jikwon_no')
    jikwon_name = request.POST.get('jikwon_name')
    jikwon_rating = Jikwon.objects.get(jikwon_no=jikwon_no).jikwon_rating
    datas = Jikwon.objects.filter(jikwon_rating=jikwon_rating)
    
    data2 = Jikwon.objects.values('jikwon_jik','buser_num')
    df = pd.DataFrame(data2)
    df.columns = ['직급','부서']
    ctab = pd.crosstab(df['직급'],df['부서'], margins=True)
    print(ctab)
    
    return render(request, 'show.html',{'datas':datas,'ctab':ctab})