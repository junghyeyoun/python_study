from django.shortcuts import render, redirect
from pro18app.models import Producttab
from django.http.response import HttpResponse, JsonResponse
import json
from django.views.generic.base import TemplateView

# Create your views here.
def Main(request):
    return render(request, 'main.html')

def List(request):
    category = request.GET['category']
    print(category)
    pdata = Producttab.objects.filter(category=category)
    datas = []
    for p in pdata:
        dicData = {'pname':p.pname,'description':p.description,'price':p.price,'stock':p.stock}
        datas.append(dicData)
        
    return HttpResponse(json.dumps(datas), content_type='application/json')

def Seller(request):
    return render(request, 'seller.html')

def ListAll(request):
    padata = Producttab.objects.all()
    print(padata)
    datas = []
    for p in padata:
        dicData = {'id':p.id,'category':p.category,'pname':p.pname,'price':p.price,'stock':p.stock,'description':p.description}
        datas.append(dicData) 
        
    return HttpResponse(json.dumps(datas), content_type='application/json')    

def Insert(request):
    if request.method == "GET":
        # POST 요청으로 들어온 데이터 추출
        category = request.GET.get('category')
        pname = request.GET.get('pname')
        price = request.GET.get('price')
        stock = request.GET.get('stock')
        description = request.GET.get('description')

        # 데이터베이스에 새 상품 추가
        product = Producttab(
            category=category,
            pname=pname,
            price=price,
            stock=stock,
            description=description
        )
        product.save()

        return JsonResponse({'message': '상품이 추가되었습니다.'})
    else:
        return JsonResponse({'message': 'GET 요청이 필요합니다.'}, status=400)







