from django.db import models
from django.db.models import Max
'''
Each Courses are either from SEPS or University General Education or from CSE core courses 
and a student must have to maintain a specific CGPA in these category in the end of the degree

'''
class Student(models.Model):
    uni_id = models.IntegerField(unique=True, primary_key=True)
    fullname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    cgpa = models.FloatField(default=0.00)
    total_credits = models.FloatField(default=0.0)
    sepscgpa = models.FloatField(default=0.0)
    corecgpa = models.FloatField(default=0.0)
    unicgpa = models.FloatField(default=0.0)
    semunmber = models.IntegerField(default=0)
    '''credits = models.IntegerField(default=0)
    software = models.IntegerField(default=0)
    hardware = models.IntegerField(default=0)
    math = models.IntegerField(default=0)
    literature = models.IntegerField(default=0)'''


    def updatecgpa(self):
        total_credit = 0
        m = 0

        grd = Grades.objects.filter(Student_id=self.uni_id)

        for g in grd:
            if (g.grade != 'N'):
                cr = Courses.objects.get(coursename=g.Course_name)
                total_credit = total_credit + cr.credits
                m = m + g.grdpa * cr.credits
        if total_credit!=0:
            self.cgpa = m / total_credit
        else:
            self.cgpa = 0
        self.total_credits= total_credit
        self.save()
