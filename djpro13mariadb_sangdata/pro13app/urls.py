from django.urls import path
from pro13app import views

urlpatterns = [ 
    path('list', views.ListFunc),
    path('insert', views.InsertFunc),
    path('insertok', views.InsertOkFunc),
    path('update', views.UpdateFunc),
    path('updateok', views.UpdateOkFunc), 
    path('delete', views.DeleteFunc),
    
]
