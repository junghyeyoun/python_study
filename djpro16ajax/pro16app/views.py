from django.shortcuts import render
import json
from django.http.response import HttpResponse
from doc.pycurl.examples.quickstart.response_headers import content_type

# dict data
lan = {
    'id':123,
    'name':'파이썬',
    'history': [
        {'date':'2023-10-25','exam':'basic'},
        {'date':'2023-10-26','exam':'django'},
        ]
}

def testFunc():
    print(type(lan)) # <class 'dict'>
    
    # python object(dict, list, tuple ...)를 문자열로 변환 : json encoding
    # json 모양의 문자열을 python object(dict)로 변환 : json decoding
    
    # json encoding
    jsonString = json.dumps(lan)  
    print(jsonString)
    print(type(jsonString)) # <class 'str'>
    jsonString = json.dumps(lan, indent=4) # 들여쓰기 되서 출력됨
    print(jsonString)
    # print(jsonString['name']) # err
    print('***'*10)
    
    # json decoding
    dicData = json.loads(jsonString)
    print(dicData)
    print(type(dicData)) # <class 'dict'>
    print(dicData['name']) # 파이썬
    for h in dicData['history']:
        print(h['date'],h['exam'])
     
# Create your views here.

def MainFunc(request):
    testFunc()
    return render(request,'abc.html')

def Func1(request):
    msg = request.GET.get('msg')
    msg = 'nice' + msg
    print(msg)
    context = {'key':msg}
    return HttpResponse(json.dumps(context), content_type="application/json")

def Func2(request):
    mydata = [
        {'irum':'tom1','nai':22},
        {'irum':'tom2','nai':23},
        {'irum':'tom3','nai':24},
    ]
    return HttpResponse(json.dumps(mydata), content_type="application/json")

