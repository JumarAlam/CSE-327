
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





