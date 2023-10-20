from django.shortcuts import render
import random

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def SelectFunc(request):
    r = random.randint(1, 100)
    if r%2 == 0:
        img = '/static/images/men.png'
        gen = '남자'
    elif r%2 !=0:
        img = '/static/images/women.png'
        gen = '여자'
        
    
    return render(request, 'show.html',{'img':img,'gen':gen})