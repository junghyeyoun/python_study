from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
def MainFunc(request):
    return render(request, 'index.html')

class Callview(TemplateView):
    template_name = 'callget.html'
    
def InsertFunc(request):
    if request.method =='GET':
        return render(request, 'insert.html')
    elif request.method == 'POST':
        irum = request.POST.get("name") # java : request.getParameter("name")
        irum = irum + " : 내 친구"
        return render(request, 'list.html', {'irum':irum})