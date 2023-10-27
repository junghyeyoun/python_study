from django.urls import path
from myvote import views

urlpatterns = [
    
    # gogo/
    path('', views.DispFunc, name='disp'),
    
    # 인자 컨버터 : <type><name> gogo/1 or gogo/2
    path('<int:question_id>', views.DetailFunc, name='detail'), 
    
    # gogo/1/vote
    path('<int:question_id>/vote', views.VoteFunc, name='vote'), 
    
    # gogo/1/result
    path('<int:question_id>/results', views.ResultFunc, name='results'),

    
]   