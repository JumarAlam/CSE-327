from django.db import models
from django.db.models import Max
'''
Each Courses are either from SEPS or University General Education or from CSE core courses 
and a student must have to maintain a specific CGPA in these category in the end of the degree
'''


class EvaluationScripts(models.Model):
    #eval_id = models.AutoField(unique=True, primary_key=True)
    faculty_name = models.CharField(max_length= 200)
    option1_input = models.CharField(max_length= 100)
    option2_input = models.CharField(max_length= 100)
    option3_input = models.CharField(max_length= 100)
    option4_input = models.CharField(max_length= 100)
    option5_input = models.CharField(max_length= 100)
    option6_input = models.CharField(max_length= 100)
    commentinput = models.CharField(max_length= 1000)
    submitter_id = models.IntegerField()
