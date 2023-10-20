from django.shortcuts import render
from pro08app.models import Article
# Create your views here.

def Main(request):
    return render(request, 'main.html' ) 

def DbShow(request):
    datas = Article.objects.all()   # 논리적인 테이블과 매핑
    print(datas) # QuerySet type
    print(datas[0].name)
    return render(request, 'list.html', {'datas': datas})
