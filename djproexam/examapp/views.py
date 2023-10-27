from django.shortcuts import render

# Create your views here.

def inputFunc(request):
    return render(request, 'input.html')

def abc(request):
    su = int(request.POST.get('su'))  
    jsu = 0
    while su > 0:  
        su = su // 10  
        jsu += 1  
    return render(request, 'show.html', {'jsu': jsu,'su':int(request.POST.get('su'))  })
