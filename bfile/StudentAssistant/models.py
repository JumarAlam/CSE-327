from django.db import models
from django.db.models import Max
'''
Each Courses are either from SEPS or University General Education or from CSE core courses 
and a student must have to maintain a specific CGPA in these category in the end of the degree
model is the interface student is the child class
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


class Courses (models.Model):
    pass


'''
'''


class ComplainBox(models.Model):
    Complain_number = models.AutoField(unique=True, primary_key=True)
    Complaining_person = models.CharField(max_length=30)
    Complainer_email = models.CharField(max_length=40)
    message = models.CharField(max_length=300)
