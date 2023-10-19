"""
URL configuration for djpro03 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls.conf import include
from pro03app import views
from pro03app.views import Callview

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path('',views.MainFunc),      #  Function views
    path('my/callget',Callview.as_view()), # Class-based views
    path('our/',include('pro03app.urls')), # Including another URLconf
]
