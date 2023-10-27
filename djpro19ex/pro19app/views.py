from django.shortcuts import render, redirect
from pro19app.models import Producttab
from django.http.response import HttpResponse
import json

# Create your views here.

def Main(request):
    return render(request, 'main.html')

def Burger(request):
    pdata = Producttab.objects.filter(category='버거')
    datas = []
    for p in pdata:
        dic = {'pname':p.pname,'description':p.description,'price':p.price, 'stock':p.stock}
        datas.append(dic)
        
    return HttpResponse(json.dumps(datas), content_type="application/json")

def Soda(request):
    pdata = Producttab.objects.filter(category='음료')
    datas = []
    for p in pdata:
        dic = {'pname':p.pname,'description':p.description,'price':p.price, 'stock':p.stock}
        datas.append(dic)
        
    return HttpResponse(json.dumps(datas), content_type="application/json")

def Admin(request):
    return render(request, 'adminpage.html')

def List(request):
    datas = Producttab.objects.all()
    
    return render(request, 'list.html', {'datas':datas})

def Insert(request):
    return render(request, 'insert.html')

def InsertOk(request):
    if request.method == 'POST':

        Producttab(
            category = request.POST.get('category'),
            pname = request.POST.get('pname'),
            price = request.POST.get('price'),
            stock = request.POST.get('stock'),
            description = request.POST.get('description'),
        ).save()
    return redirect("/adminpage")

