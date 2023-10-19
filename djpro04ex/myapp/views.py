from django.shortcuts import render
import random

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def SelectFunc(request):
    r = random.randint(1, 100)
    img = ''
    if r%2 == 0:
        img = '/static/images/men.png'
    elif r%2 !=0:
        img = '/static/images/women.png'
        
    
    return render(request, 'show.html',{'img':img})