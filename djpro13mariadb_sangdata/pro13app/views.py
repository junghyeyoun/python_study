from django.shortcuts import render, redirect
import MySQLdb
from pro13app.models import Sangdata
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'seoho123',
    'database':'test',
    'port':3306, # 안쓰면 기본값 3306
    'charset':'utf8',
    'use_unicode':True
}

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    """
    # sql문 이용해서 하기 - 장고 사용하지 않고 원래 방법
    try:
        conn = MySQLdb.connect(**config) 
        cursor = conn.cursor() 
        sql = "select * from sangdata"
        cursor.execute(sql)
        datas = cursor.fetchall()
        print(datas) # ((1, '장갑', 3, 10000), (2, '물티슈', 10, 2000), (3, '가죽장갑', 10, 50000), (4, '가죽점퍼', 5, 650000), (5, '지우개', 12, 1000), (6, '물병', 10, 2000), (7, '지우개', 10, 1000))
        print(type(datas)) # <class 'tuple'>
        
        return render(request, 'list.html',{'datas':datas})
    
    except Exception as err:
        print('에러 : ',err)
        conn.rollback()
    finally:
        conn.close()
    """
    
    # 페이징 안한 경우
    """
    datas = Sangdata.objects.all()
    print(datas) 
    print(type(datas)) # <class 'django.db.models.query.QuerySet'>
    return render(request, 'list.html',{'datas':datas})
    """
    
    # 페이징 한 경우
    datas = Sangdata.objects.all().order_by('-code')
    paginator = Paginator(datas, 5) # 페이지당 5행씩 출력
    # print(paginator) # <django.core.paginator.Paginator object at 0x000002C087669990>
    try:
        page = request.GET.get('page')
    except:
        page = 1
        
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages())
        
    # 개별 페지이 표시 작업용
    allpage = range(paginator.num_pages+1)
    print('allpage : ',allpage) # allpage :  range(0, 3)
    return render(request,'list2.html',{'datas':data, 'allpage':allpage})
    
def InsertFunc(request):
    return render(request,'insert.html')

def InsertOkFunc(request):
    if request.method == 'POST':
        code = request.POST.get("code")
        # 새 상품 code 유무 인증 후 insert 진행
        try:
            Sangdata.objects.get(code=code)
            return render(request, 'insert.html', {'msg':'이미 등록된 번호입니다'})
        except Exception:
            # 추가 작업
            Sangdata(
                code = code,
                sang = request.POST.get("sang"),
                su = request.POST.get("su"),
                dan = request.POST.get("dan"),
                
            ).save()
            return HttpResponseRedirect("/sangpum/list")


def UpdateFunc(request):
    update = Sangdata.objects.get(code=request.GET.get("code"))
    return render(request, 'update.html', {'data':update})

def UpdateOkFunc(request):
    if request.method == 'POST':
        upRecord = Sangdata.objects.get(code=request.POST.get("code"))
        upRecord.code = request.POST.get("code")
        upRecord.sang = request.POST.get("sang")
        upRecord.su = request.POST.get("su")
        upRecord.dan= request.POST.get("dan")
        upRecord.save()
        
    return redirect('/sangpum/list')  # 수정 후 목록보기

        
def DeleteFunc(request):
    delRecord = Sangdata.objects.get(code=request.GET.get("code"))
    delRecord.delete()
    return redirect('/sangpum/list')