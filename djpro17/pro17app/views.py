from django.shortcuts import render
from pro17app.models import Sangdata
from django.http.response import HttpResponse
import json

# Create your views here.
def MainFunc(request):
    return render(request,'main.html')

def ListFunc(request):
    return render(request,'list.html')

def DbFunc(request):
    sdata = Sangdata.objects.all()
    datas = []
    for s in sdata:
        dic = {'code':s.code,'sang':s.sang,'su':s.su,'dan':s.dan}
        datas.append(dic)
        
    return HttpResponse(json.dumps(datas), content_type = "applicataion/json")