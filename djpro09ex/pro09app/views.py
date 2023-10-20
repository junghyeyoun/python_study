from django.shortcuts import render
from pro09app.models import Friend

# Create your views here.

def Main(request):
    return render(request, 'main.html' ) 

def DbShow(request):
    datas = Friend.objects.all()
    su = Friend.objects.count()
    print(su)
    return render(request, 'list.html',{'datas':datas,'su':su})
