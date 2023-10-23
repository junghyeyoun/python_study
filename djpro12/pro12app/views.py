from django.shortcuts import render
from pro12app.models import Maker
from pro12app.models import Product
from django.db.models.aggregates import Count, Avg, Sum, StdDev

# Create your views here.
def Main (request):
    return render(request, 'main.html')

def List1 (request):
    makers = Maker.objects.all()
    
    return render(request, 'list1.html',{'makers':makers})

def List2 (request):
    products = Product.objects.all()
    pcount = len(products)
    
    # ORM 함수 연습
    print(products)
    print(products.values_list())
    
    print(products.all().count())  
    print(products.aggregate(Count('pprice')))
    print(products.aggregate(Sum('pprice')))
    print(products.aggregate(Sum('pprice'))['pprice__sum'])
    
    print(products.aggregate(Avg('pprice')))
    print(products.aggregate(StdDev('pprice')))
    
    aa = products.filter(pname = '농구화') # 농구화만 보기
    print(aa)
    for a in aa.values_list():
        print(a)
    
    print()
    aa = products.exclude(pname = '농구화') # 농구화만 제외
    print(aa)
    for a in aa.values_list():
        print(a)
    
    return render(request,'list2.html',{'products':products,'pcount':pcount})

def List3(request):
    mid = request.GET.get('id')
    products = Product.objects.filter(pmaker_name=mid)
    pcount = len(products)
    return render(request, "list2.html", {'products':products, 'pcount':pcount})
