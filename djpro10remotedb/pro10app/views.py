from django.shortcuts import render, redirect
from pro10app.models import Guest
from django.utils import timezone
from datetime import datetime
from django.http.response import HttpResponseRedirect


# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    print(Guest.objects.filter(title__contains='연습'))
    print(Guest.objects.filter(title='연습'))
    print(Guest.objects.get(id=1))
    
    # select * from pro10app_guest 
    gdatas = Guest.objects.all()
    # 정렬 방법 2 : 
    # gdatas = Guest.objects.all().order_by('-id') # - 붙이면 desc
    # gdatas = Guest.objects.all().order_by('title','-id') # title은 asc, id는 desc => title 같은게 있다면 id로 desc
    # gdatas = Guest.objects.all().order_by('-id')[0:2] # desc으로 뒤에서 두개만
    return render(request,'list.html',{'gdatas':gdatas})

def InsertFunc(request):
    return render(request,'insert.html')

def InsertOkFunc(requset):
    if requset.method == 'POST':
        # print(requset.POST.get('title'))
        # print(requset.POST['title']) 
        # insert into pro10app_guest (...
        Guest(
            title = requset.POST.get('title'),
            content = requset.POST.get('content'),
            regdate = datetime.now()
           #  regdate = timezone.now()
            ).save()
        
        # 수정 
        # Guest(
            # g=Guest.objects.get(id=수정할 번호)
            # g.title=requset.POST.get('title'),
            # g.content=requset.POST.get('content'),
            # regdate = timezone.now()
            
        # 삭제
            # g = Guest.objects.get(id=삭제할 번호)
            # g.delete()
            # ).save()
            
    # return HttpResponseRedirect ("/guest/select")
    return redirect ("/guest/select") # 추가후 목록보기
    
