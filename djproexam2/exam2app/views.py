from django.shortcuts import render
from exam2app.models import Jikwon, Gogek

# Create your views here.
def inputFunc(request):
    return render(request, 'input.html')

def showFunc(request):
    gogek_name = request.POST.get('gogek_name')
    gogek_tel = request.POST.get('gogek_tel')
    
    try:
        gogek = Gogek.objects.get(gogek_name=gogek_name, gogek_tel=gogek_tel)
        gogek_damsano = gogek.gogek_damsano
        data = Jikwon.objects.filter(jikwon_no=gogek_damsano) 
        
        return render(request, 'show.html', {'data': data})
    except Exception as e:
        print('오류 : ', e)

