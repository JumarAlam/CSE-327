
from django.shortcuts import render
#from .forms import *
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from pyknow import *
from .engine import *
from django.contrib import sessions
from .prerequisites import Prereq
from .numofcourses import Numofcrs
import math
'''
generates Views
every method takes a http request object as an argument


'''



class StudentAssistant:

    def gradecal(request): # Added by Jumar 
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

                return HttpResponseRedirect('/gradecal')

    # added by Jumar upto this




    def index(request):
        '''
        this will Render the home page

        return : render object , welcome.html
        '''
        return HttpResponse("<h1>This thing is working properly</h1>")


    #generates facts & creates inference engine of prerequisites
   
    def courseadvise(request):
        '''
        return : render object, courseadvisor.html
        '''
        if request.session.has_key('uni_id'):
            l=[]  #list of courses he can take
            l.clear()
            seps = []
            seps.clear()
            cse = []
            cse.clear()
            uni = []
            uni.clear()
            uid = request.session['uni_id']
            std = Student.objects.get(uni_id=uid)
            std.getsemnumber()
            grdobj = Grades.objects.filter(Student_id= uid)
            engine = Prereq()
            engine.reset()
            for g in grdobj:

                engine.declare(Fact(g.Course_name,grade=g.grade))
            engine.declare(Fact(credit=std.total_credits))
            engine.run()

            #complicated sector
            crdengine = Numofcrs()
            crdengine.reset()
            crdengine.declare(Fact(cgpa=std.cgpa))
            crdengine.declare(Fact(semnum= std.semunmber))
            crdengine.declare(Fact(credits= std.total_credits))
            crdengine.run()
            dat = crdengine.numbcrs() 
            semcr = {1:11, 2: 12, 3: 14, 4:13, 5:13, 6:7, 7:14, 8:12, 9:13, 10:9, 11:7.5, 12: 7.5 }
            expectations = {1:0, 2:11, 3:23, 4:37, 5:50, 6:63, 7:70, 8:84, 9:96, 10:109, 11:118, 12:125.5}
            smst = (std.semunmber)
            if smst>12:
                maxcrd = dat
            else:
                if std.total_credits >= expectations[smst]:
                    maxcrd= semcr[std.semunmber]
                else:
                    maxcrd= dat

            #maxcrd= #max credit a student can take
            cfts = 0 # total credit he should be taking
            n = [] # list of courses he should be taking
            t = engine.listpass()
            a1 = engine.unicourses()
            a2 = engine.SEPScourses()
            a3 = engine.corecourses()
            p = 13
            for j1 in a1:
                unicrc = Courses.objects.get(coursename=j1)
                prio1 = unicrc.priority
                uni.append((prio1,unicrc.coursetitle))
            for j2 in a2:
                sepscrc = Courses.objects.get(coursename=j2)
                prio2 = sepscrc.priority
                seps.append((prio2, sepscrc.coursetitle))

            for j3 in a3:
                csecrc = Courses.objects.get(coursename=j3)
                prio3 = csecrc.priority
                cse.append((prio3, csecrc.coursetitle))


            for m in t:
                crs = Courses.objects.get(coursename=m)
                if p >= crs.priority:
                    p = crs.priority
            catprio = {'CORE':1,'SEPS':2,'UNI':3, 'CAPS':4, 'TRAIL':5, 'OPEN':6}
            for m1 in t:
                crss = Courses.objects.get(coursename=m1)
                m2 = catprio[crss.category]
                ch = crss.credits
                print(crss.category)
                l.append((crss.priority, m2 ,ch, crss.coursetitle))
                #if p == crss.priority:
                #   l.append((crss.priority,m1))
            a1.clear()
            a2.clear()
            a3.clear()
            t.clear()
            l= sorted(l)
            '''Not perfectly Working '''
            for i in l:
                if cfts <= maxcrd:
                    n.append(i[3])
                    cfts = cfts + i[2]
                else:
                    n1 = n.pop()

                    cfts -=i[2]
                    break





        return render(request, "courseadvisor.html", {'suggested': n,'totcred':cfts,'dat': l, 'csecore': sorted(cse), 'sepscore': sorted(seps), 'unicore': sorted(uni)})



    def showgradpath(request):
        '''
        Shows full Graduation path as from the point of a students current situation

        return: render type, coursepath.html

        '''
        if request.session.has_key("uni_id"):
            lst = []
            i=1
            stdid = request.session['uni_id']
            std = Student.objects.get(uni_id= stdid )
            grdobj = Grades.objects.filter(Student_id=stdid)
            for grd in grdobj:
                c = Courses.objects.get(coursename= grd.Course_name)
                lst.append([c.credits,grd.Course_name,grd.grade])
                i=i+1
            obj = Gradepath(lst,std.total_credits)
            d = obj.returncoursepath()
            print(d)

            return render(request,'coursepath.html',{'data':d})
