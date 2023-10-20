from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect

# Create your views here.
def mainFunc(request):
    return render(request, "main.html")    # forward

def selectOsFunc(request):
    # print('request.GET :', request.GET)  # <QueryDict: {}>
    if 'favorite_os' in request.GET:
        print(request.GET["favorite_os"])
        request.session["f_os"] = request.GET["favorite_os"]   # session에 값을 저장
        return HttpResponseRedirect("showos")     # redirect
    else:
        return render(request, "selectos.html")
    
def showOsFunc(request):
    # print("showOsFunc 도착")
    dict_context = {}
    
    if "f_os" in request.session:
        print('유효시간 : ', request.session.get_expiry_age())
        dict_context['sel_os'] = request.session["f_os"]
        dict_context['message'] = '그대가 선택한 운영체제는 %s'%request.session["f_os"] # session
    else:
        dict_context['sel_os'] = None
        dict_context['message'] = '운영체제를 선택하지 않았군요'
        
    # del request.session["f_os"]   # 특정 키를 가진 세션을 삭제
    request.session.set_expiry(5)
        
    return render(request, 'show.html', dict_context)
