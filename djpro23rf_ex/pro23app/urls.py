from django.urls import path
from pro23app import views

urlpatterns = [    
    path('list',views.ListFunc),
    path('show',views.ShowFunc),
]
