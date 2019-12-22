"""StudentAssistant URL Configuration
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
    path('', sa.index, name="index" ),
    path('register/', sa.register, name= 'register'),
    path('login/', sa.login, name= 'login'),
    path('logact/', sa.loginaction, name = "loginaction"),
    path('regact/', sa.registeraction, name = 'registeraction'),
    path('profile/', sa.profile, name= 'userprofile'),
    path('about/', sa.about, name = 'aboutactionlistener'),
    
    path('gradecal/', sa.gradecal, name='grade calcualtor'),
    path('gradecal2/', sa.gradecalaction, name='grade calcualtor action'),
    path('gradhist/',sa.gradehistory, name='Grade History'),
    path('suggestion/',sa.courseadvise, name='Course Advisor'),
    path('grapath/', sa.showgradpath, name= 'Course Path'),
    path('logout/', sa.logout, name = 'logout'),
    path('retakes/', sa.retakelist, name= 'retake list'),

    ###
    path('complain/', sa.complain, name='complain box'),
    path('complainaction/', sa.complainActionListener, name='complain box Action Listener'),
    path('lostandfound/', sa.lostandfound, name = 'lost and found'),
    path('lostandfoundaction/', sa.lostandfoundaction, name = 'lost and found'),

    ###

    path('facultyevaluation/', sa.eval, name = 'facultyevaluation'),
    path('evalact/', sa.evalact, name = 'facultyevaluationactionlistener'),

]

