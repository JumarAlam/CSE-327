
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
from .retakeengine import *
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

    def gradecal(request):
        if request.session.has_key('uni_id'):
            form = GradeForm()
            return render(request,"gradecalculate.html", {'form':form})
        else:
            return HttpResponseRedirect('/login')

    def gradecalaction(request):    #Added By Jumar
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

    ###############################################################################################       
    def index(request):

        '''
        this will Render the home page

        return : render object , welcome.html
        '''

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

        '''
        Loads profile and student Information

        Return: Render Object, renders profile.html
        '''
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

        '''

        Deletes the session for the Student User

        Return: Ridirects to login.html


        '''
        try:
            del request.session['uni_id']
        except:
            return HttpResponse("<h1> Could not logout for some reason</h1>")
        return HttpResponseRedirect('/login')

    """
    """
    
    def gradehistory(request):
        if request.session.has_key('uni_id'):
            uid = request.session['uni_id']
            grdobj = Grades.objects.filter(Student_id = uid)
            d= []
            for g in grdobj:
                if(g.grade!= 'N'):
                    d.append(g)

            return render(request,'Gradehistory.html',{'gradedata': d})


    ################################################################################################
    
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
                if p >= int(crs.priority):
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


    #Add docs

    def lostandfound(request):
    	if request.session.has_key("uni_id"):
            form = LostForm()
            lostlist = LostandFound.objects.filter(status = False)
            return render(request, 'lostnfound.html', {'form':form, 'lostinfo': lostlist})


    	else:
    		return HttpResponse('<h1> you have to login to report lost and found</h1>')

    	

    def lostandfoundaction(request):
    	if request.session.has_key("uni_id"):
    		form = LostForm(request.POST)
    		if form.is_valid():
    			convert_items = {"1":'ID_Card', "2": 'Pen-Drive', "3":'Others'}
    			itemtype = form.cleaned_data['itemtype']
    			description = form.cleaned_data['description']
    			converted_itemtype = convert_items[itemtype]
    			university_id =  request.session['uni_id']
    			studentObject = Student.objects.get(uni_id= university_id)
    			email = studentObject.email

    			try:
    				loser_Id = form.cleaned_data['loser_id']
    			except Exception as e:
    				loser_Id = None

    			lost_object = LostandFound(finders_id=university_id, itemtype=converted_itemtype, loser_id=loser_Id, finder_contact_email=email,lost_item=description, status=False)
    			lost_object.save()
                
    			return HttpResponseRedirect('/lostandfound')
    			
#################SHAHRIAR FILES #########################

    # creating inference engine of pre req

    ''' complain box requests forms and views.
    '''

    def complain(request):
        form = ComplaintForm()  # generating form from forms.py
        return render(request, 'complain.html', {'form': form})

    '''
        get form and send the redirects to complain page
    '''

    def complainActionListener(request):
        form = ComplaintForm(request.POST)  # CF class from form file
        if form.is_valid():  # validation check
            fullname = form.cleaned_data['fullname']
            email = form.cleaned_data['email']
            comment = form.cleaned_data['comment']

            complainObject = ComplainBox(
                Complaining_person=fullname, Complainer_email=email, message=comment)
            complainObject.save()
        return HttpResponseRedirect('/complain')
    '''
    extract the retake list from retakes inference engine and
    '''

    def retakelist(request):
        if request.session.has_key("uni_id"):  # session check
            stdid = request.session['uni_id']
            rtk = Retakecrs()
            rtk.resetengine()
            grd = Grades.objects.filter(Student_id=stdid)
            for g in grd:
                cr = Courses.objects.get(coursename=g.Course_name)
                rtk.setfactdatalist([g.Course_name, g.grade, cr.category])
            rtk.definefacts()
            l = []
            s = []
            s.clear()

            l = rtk.runes()
            for d in l:
                s.append(d)
            l.clear()

            return render(request, 'retakes.html', {'retakables': s})





 



