"""v1 URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from .views import StudentAssistant as sa
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

    # login logout register landing
    path('', sa.index, name="index" ),
    path('register/', sa.register, name= 'register'),
    path('login/', sa.login, name= 'login'),
    path('logact/', sa.loginaction, name = "loginaction"),
    path('regact/', sa.registeraction, name = 'registeraction'),
    path('logout/', sa.logout, name = 'logout'),


    path('profile/', sa.profile, name= 'userprofile'),
    
    
    
    #Tanjeeb
    path('facultyevaluation/', sa.eval, name = 'facultyevaluation'),
    path('evalact/', sa.evalact, name = 'facultyevaluationactionlistener'),

    # Nusher
    path('suggestion/', sa.courseadvise, name = 'suggested courses'),
    path('gradecal2/', sa.gradecalaction, name='grade calcualtor action'),

    #Jumer 
    #path('lostnfound/', sa.lostnfound, name='lost and found action'), #views are not added...
    path('gradpath/', sa.showgradpath, name='shows Full graduation Path')
]
