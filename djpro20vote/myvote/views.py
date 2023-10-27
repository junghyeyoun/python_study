from django.shortcuts import render, get_object_or_404
from myvote.models import Question, Choice
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.urls.base import reverse

# Create your views here.
def MainFunc(request):
    return render(request,'main.html')

def DispFunc(request):
    q_list = Question.objects.all().order_by('pub_date','id')
    context = {'q_list':q_list}
    return render(request,'display.html',context)

def DetailFunc(request, question_id):
    """
    # print('question_id : ',question_id)
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("질문 항목 파일이 없습니다.")
        """
    # get_object_or_404 :  Django에서 자주 사용되는 유틸리티 함수 중 하나로, 주어진 모델에서 특정 조건을 만족하는 객체를 검색하는 데 사용됩니다. 
    # 만약 해당 조건을 만족하는 객체를 찾을 수 없을 때, 이 함수는 HTTP 404 오류를 발생시킵니다. 
    # 일반적으로 이 함수는 웹 애플리케이션의 뷰 함수에서 객체를 가져올 때 사용됩니다.
    question = get_object_or_404(Question, pk=question_id)
    print(question.question_text)
    print(question.pub_date)
    print(question) # question_text가 찍힘
    print(question.choice_set.all()) # <QuerySet [<Choice: Choice object (1)>, <Choice: Choice object (2)>, <Choice: Choice object (3)>]>
    for cho in question.choice_set.all():
        print(cho.choice_text) 
    
    return render(request,'detail.html',{'question':question})

def VoteFunc(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        sel_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {'question':question, 'err_msg':'1개의 항목을 선택하세요'})

    sel_choice.votes += 1
    sel_choice.save()   # 선택항목을 1씩 늘린 후 테이블 수정
    print(reverse('results', args=(question.id,)))   # /gogo/1/results
    
    return HttpResponseRedirect(reverse('results', args=(question.id,)))



def ResultFunc(request, question_id):
    # return HttpResponse('bb')
    question = get_object_or_404(Question, pk=question_id)
    
    return render(request,'result.html',{'question':question})