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
    page = request.GET.get('page')
    data = BoardTab.objects.get(id=request.GET.get('id'))
    data.readcnt = data.readcnt + 1
    data.save() # 조회수 갱신
    
    return render(request, 'content.html',{'data':data,'page':page})

def updateFunc(request):
    if request.method == 'GET':
        try:
            data = BoardTab.objects.get(id=request.GET.get('id'))
            return render(request, 'update.html',{'data':data})
        except Exception as e:
            print('수정 자료 읽기 오류 : ',e)
            return render(request,'error.html')
    elif request.method == 'POST':
        try:
            updata = BoardTab.objects.get(id=request.POST.get('id'))
            # 비밀번호 비교
            if updata.passwd == request.POST.get('up_passwd'):
                updata.name = request.POST.get('name')
                updata.mail = request.POST.get('mail')
                updata.title = request.POST.get('title')
                updata.cont = request.POST.get('cont')
                updata.save()
                return redirect('/board/list')
            else:
                return render(request, 'update.html',{'data':updata,'upmsg':'비밀번호 불일치!'})
        except Exception as e:
            print('수정 자료 처리 오류 : ',e)
            return render(request,'error.html')
    

def deleteFunc(request):
    if request.method == 'GET':
        try:
            deldata = BoardTab.objects.get(id=request.GET.get('id'))
            return render(request, 'delete.html',{'data':deldata})
        except Exception as e:
            print('삭제 자료 읽기 오류 : ',e)
            return render(request,'error.html')
    elif request.method == 'POST':
        try:
            deldata = BoardTab.objects.get(id=request.POST.get('id'))
            if deldata.passwd == request.POST.get('del_passwd'):
                deldata.delete()
                return redirect('/board/list') # 삭제후 목록 보기
            else:
                return render(request,'error.html')
        except Exception as e:
            print('삭제 자료 처리 오류 : ',e)
            return render(request,'error.html')
    return render(request, )