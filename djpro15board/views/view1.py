from django.shortcuts import render, redirect
from myboard.models import BoardTab
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from datetime import datetime

# Create your views here.
def mainFunc(request):
    imsi = "<div><h2>메인화면</h2></div>"  # HTML 형식의 문서를 전송
    return render(request,'main.html',{'maintag':imsi})

def listFunc(request):
    data_all = BoardTab.objects.all().order_by('-gnum','onum')
    
    paginator = Paginator(data_all, 5)     # 페이지 당 5명씩 출력
    # print(paginator)
    try:
        page = request.GET.get('page')
    except:
        page = 1

    try:
        datas = paginator.page(page)
    except PageNotAnInteger:
        datas = paginator.page(1)
    except EmptyPage:
        datas = paginator.page(paginator.num_pages())
        
    # 개별 페이지 표시 작업용
    allpage = range(paginator.num_pages + 1)
    # allpage = range(4)와 같다 11개 글 기준 
    #print(allpage)  # range(0, 4)
        
    return render(request, 'board.html',{'datas':datas})

def insertFunc(request):
    if request.method == 'GET':
        return render(request, 'insert.html')
    elif request.method == 'POST':
        try:
            gbun = 1  #Group number
            datas = BoardTab.objects.all()
            if datas.count() != 0:
                gbun = BoardTab.objects.latest('id').id + 1
                
            BoardTab(
                name = request.POST.get('name'),
                passwd = request.POST.get('passwd'),
                mail = request.POST.get('mail'),
                title = request.POST.get('title'),
                cont = request.POST.get('cont'),
                bip = request.META['REMOTE_ADDR'],  # request.META.get['REMOTE_ADDR'] 
                bdate = datetime.now(),
                readcnt = 0,
                gnum = gbun,
                onum=0,
                nested=0,
            ).save()
        except Exception as e:
            print('추가 에러 : ',e)
            return render(request, 'error.html')
    return redirect('/board/list')

def searchFunc(request):
    if request.method == 'POST':
        s_type = request.POST.get('s_type')
        s_value = request.POST.get('s_value')
        # print(s_type,s_value)
        
        if s_type == 'title':
            # SQL의 LIKE 문과 같음 : 칼럼명__contains
            datas_search = BoardTab.objects.filter(title__contains=s_value).order_by('-id')
        elif s_type == 'name':
            datas_search = BoardTab.objects.filter(name__contains=s_value).order_by('-id')
        
        # 페이징
        paginator = Paginator(datas_search, 5)     # 페이지 당 5명씩 출력
        # print(paginator)
        try:
            page = request.GET.get('page')
        except:
            page = 1
    
        try:
            datas = paginator.page(page)
        except PageNotAnInteger:
            datas = paginator.page(1)
        except EmptyPage:
            datas = paginator.page(paginator.num_pages())
            
        return render(request,'board.html',{'datas':datas})

def contentFunc(request):
    return render(request, )

def updateFunc(request):
    return render(request, )

def deleteFunc(request):
    return render(request, )