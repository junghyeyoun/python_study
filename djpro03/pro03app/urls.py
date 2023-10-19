from django.urls import path
from pro03app import views
urlpatterns = [
    path('insert',views.InsertFunc),      #  Function views
]
