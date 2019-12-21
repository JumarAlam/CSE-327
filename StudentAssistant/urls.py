
"""v1 URL Configuration"""
=======
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
#from .views import Studentasist as sa
from django.urls import path
from .views  import StudentAssistant as sa

''' routing '''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sa.index, name="index" ),
   
    path('retakes/', sa.retakelist, name= 'retake list'),

    path('complain/', sa.complain, name='complain box'),
    path('complainaction/', sa.complainActionListener, name='complain box Action Listener'),
    path('gradecal2/', sa.gradecalaction, name='grade calcualtor action'),
	  path('lostnfound/', sa.lostnfound, name='lost and found action
    
]
   
"""
=======
from django.urls import path
#from . import views
from .views  import StudentAssistant as sa

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', views.index, name='landing'),
    path('gradecal2/', sa.gradecalaction, name='grade calcualtor action'),
	path('lostnfound/', sa.lostnfound, name='lost and found action'),

]
"""