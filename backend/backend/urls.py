"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from realtime import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hellofriend', views.trial ),
    path('dekho', views.kuchbhi ), 
    path('tower/details', views.towers_detail), 
    path('tower/bhavya', views.towers_bhavya), 
    path('getall', views.sports_events_get_name_poster ),
    #Proceed With Caution
    # path('difference', views.getDifference),
    # path('sendtoDb', views.sendtoDb ), 
]
