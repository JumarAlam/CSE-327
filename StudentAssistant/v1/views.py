from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from pyknow import *
from .engine import *
from django.contrib import sessions
from .prerequisites import Prereq
from .numofcourses import Numofcrs
import math









class Studentasist:

    def index(request):
        return render(request, 'welcome.html')
        #return render(request, "login/login.html")

    def login(request):
        form = LoginForm()
        return render(request, "login2.html", {"form": form})
        
        
        
    def loginaction(request):
            form = LoginForm(request.POST)
            if form.is_valid():
                uid = form.cleaned_data["user_id"]
                password = form.cleaned_data['password']
                u = Student.objects.get(uni_id = uid)
                if u.password == password:
                    request.session["uni_id"] = u.uni_id
                    return HttpResponseRedirect('/profile')
                else:
                    return HttpResponse('<h1> password or username donot match</h1><h2>are you trying to do anything naughty?</h2>')

#registers users
    def register(request):
        form = RegistrationForm()
        return render(request, "signup.html", {"form":form})

#gets the post data and creates a 46 grades data for each students
    def registeraction(request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            uid= form.cleaned_data["user_id"]
            fullname = form.cleaned_data["fullname"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            #check confirm password is similer or not
            stobj = Student(uni_id=uid,fullname=fullname,email=email,password=password)
            s = Courses.objects.all()

            for i in s:
                x = Grades(Student_id=uid, Course_name=i.coursename)
                x.save()


            stobj.save()
            return HttpResponseRedirect('/login')
            
            
            
            
    def profile(request):
        if request.session.has_key("uni_id"):
            stdid = request.session['uni_id']
            stddata = Student.objects.get(uni_id= stdid)
            stddata.updatecatcgpa('SEPS')
            stddata.updatecatcgpa('UNI')
            stddata.updatecatcgpa('CORE')
            stddata.getsemnumber()
            context = {"stinfo": stddata}
            return render(request, 'profile.html', context)
        
    
    def logout(request):
        try:
            del request.session['uni_id']
        except:
            return HttpResponse("<h1> Could not logout for some reason</h1>")
        return HttpResponseRedirect('/login')
    
    
    
    
    
    
    
    
    
    ### faculty evaluation

    def eval(request):
        if request.session.has_key('uni_id'):
            uid = request.session['uni_id']
            studentObject  = Student.objects.get(uni_id= uid)
            form = Evaluation()

            return render(request, 'eval.html', {'form': form})
        else:
            return HttpResponse('<h1>login required</h1>')

