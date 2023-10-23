from django.shortcuts import render, redirect
from pro11app.models import Family
from django.db.models.aggregates import Avg

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    fdatas = Family.objects.all()
    su = len(fdatas)
    average_age = Family.objects.aggregate(avg_age=Avg('age'))['avg_age']
    
    return render(request,'list.html',{'fdatas':fdatas, 'su':su,'average_age':average_age})
    
def InsertFunc(request):
    return render(request, 'insert.html')

def InsertOkFunc(request):
    if request.method == 'POST':
        Family(
            name = request.POST.get('name'),
            age = request.POST.get('age'),
            tel = request.POST.get('tel'),
            gen = request.POST.get('gen'),
        ).save()
        
    return redirect("/guest/select")