from django.shortcuts import render
from pro14app.models import Buser, Jikwon, Gogek
from django.db.models.expressions import Case, When, Value
from django.db.models.query_utils import Q

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def BuserFunc(request):
    datas = Buser.objects.all()
    
    return render(request, 'buser.html',{'datas':datas})

def JikwonFunc(request):
    buser_no = request.GET.get('buser_no')
    datas = Jikwon.objects.filter(buser_num=buser_no)
    
    for jikwon in datas:
        jikwon.gogek_damsano_count = jikwon.gogek_set.count()  # gogek_set은 관련된 고객을 가져옵니다
    
    return render(request, 'jikwon.html', {'datas': datas})

def GogekFunc(request):
    datas = Gogek.objects.filter(gogek_damsano=request.GET.get('jikwon_no')).annotate(
        gen=Case(
            When(
                Q(gogek_jumin__contains='-1') | Q(gogek_jumin__contains='-3'),
                then=Value('남')
            ),
            default=Value('여'),
        )
    ).order_by('gogek_name')
    
    return render(request,'gogek.html',{'datas':datas})


