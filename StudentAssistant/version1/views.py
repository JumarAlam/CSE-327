
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
# Create your views here.
#updates needed in line numbers
#42




class Studentasist:

    def gradecal(request):
        if request.session.has_key('uni_id'):
            form = GradeForm()
            return render(request,"gradecalculate.html", {'form':form})
        else:
            return HttpResponseRedirect('/login')

    #updates the grades of students
    #calculates cgpa

    def gradecalaction(request):
        grdparam = {'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'F': 0.0}
        converter = {'1':'A','2':'A-','3':'B+','4':'B','5':'B-','6':'C+','7':'C','8':'C-','9':'D+', '10':'D' }
        if request.session.has_key('uni_id'):
            uid = request.session['uni_id']
            form = GradeForm(request.POST)
            if form.is_valid():
                crsname= form.cleaned_data['coursename']
                crsgrade = form.cleaned_data['coursegrade']
                sem = form.cleaned_data['semester']
                crsgrade = converter[crsgrade]
                grdobj = Grades.objects.get(Student_id=uid, Course_name=crsname)
                grdobj.grdpa=grdparam[crsgrade]
                grdobj.grade = crsgrade
                grdobj.semnum = sem
                grdobj.save()
                std = Student.objects.get(uni_id= uid)

                std.updatecgpa()
                std.updatecatcgpa('SEPS')
                std.updatecatcgpa('UNI')
                std.updatecatcgpa('CORE')
                #cgpa update


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





