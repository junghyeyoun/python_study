from django.urls import path
from pro11app import views 


urlpatterns = [
    path('select',views.ListFunc),
    path('insert',views.InsertFunc), 
    path('insertok',views.InsertOkFunc), 
]