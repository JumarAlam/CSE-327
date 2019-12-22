'''
TODO's:
Needs to match confirm password and password values before registering
Needs to create Course Advisor Object Oriented (Done)
Needs an Expert System for Students to determine how much courses they should take(Done)
Needs to have an Expert System for Determining which courses should be retaken(Done)
Probation checker
Adding elective and capstone courses in database 
adding them into prereq Knowledge Base (Done)
Add a friggin Front end for this project (ALmost Done)
the AI needs more classifiers (working on it..)
ADD retakes/ in navbar
ADD newnav in other pages
Update 
'''

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






                '''
                total_credit = 0
                m = 0
                grd = Grades.objects.filter(Student_id=uid)
                for g in grd:
                    if (g.grade != 'N'):
                        cr = Courses.objects.get(coursename=g.Course_name)
                        total_credit = total_credit + cr.credits
                        m = m + g.grdpa * cr.credits
                cgpa = m / total_credit
                stdobj = Student.objects.get(uni_id=uid)
                stdobj.total_credits = total_credit
                stdobj.cgpa = cgpa
                stdobj.save()
'''
                return HttpResponseRedirect('/gradecal')
           
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
        
    def evalact(request):
            if request.session.has_key('uni_id'):
                uid = request.session['uni_id']
                studentObject  = Student.objects.get(uni_id= uid)
                form = Evaluation(request.POST)
                print(form.errors)
                

                if form.is_valid():
                    convert_items = {'1': 'Agree','2': 'Neutral', '3':'Disagree'}
                    faculty_name = form.cleaned_data['facultyname']
                    option1 = form.cleaned_data['option1']
                    option1 = convert_items[option1]

                    option2 = form.cleaned_data['option2']
                    option2 = convert_items[option2]

                    option3 = form.cleaned_data['option3']
                    option3 = convert_items[option3]

                    option4 = form.cleaned_data['option4']
                    option4 = convert_items[option4]

                    option5 = form.cleaned_data['option5']
                    option5 = convert_items[option5]

                    option6 = form.cleaned_data['option6']
                    option6 = convert_items[option6]

                    comment = form.cleaned_data['comment']

                    print(faculty_name+' ' + option1+' ' + comment +' ' +str(uid))
                        #option6 = convert_items[option6]
                    newEvalObject = EvaluationScripts(faculty_name=faculty_name, option1_input=option1, option2_input=option2, option3_input=option3, option4_input=option4, option5_input=option5, option6_input=option6, commentinput=comment, submitter_id=uid)
                    newEvalObject.save()
                return HttpResponseRedirect('/facultyevaluation')
            else:
                return HttpResponse('<h1> Not working</h1>')
                        

