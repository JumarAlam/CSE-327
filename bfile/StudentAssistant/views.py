from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from pyknow import *
#from .engine import *
from django.contrib import sessions
import math


class Studentasist:
    ''' takes you to landing page views function
    '''

    def index(request):
        return render(request, 'welcome.html')
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
        if form.is_valid:  # validation check
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
