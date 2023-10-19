from django.urls import path
from myapp import views
urlpatterns = [
    path('select',views.SelectFunc),       #  Function views
]
