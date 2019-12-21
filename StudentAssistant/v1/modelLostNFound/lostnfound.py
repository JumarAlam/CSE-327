from django.db import models
from django.db.models import Max

class LostandFound(models.Model):
	"""
	LostandFound class
	Attributes: lost_id, finders_id, itemtype, loser_id, finder_contact_email, lost_item, status
	"""
    lost_id = models.AutoField(unique=True, primary_key= True)
    finders_id = models.IntegerField(null= False)
    itemtype = models.CharField(max_length=30)
    loser_id = models.IntegerField(null=True, default=None)
    finder_contact_email = models.CharField(max_length=40)
    lost_item = models.CharField(max_length=400)
    status = models.BooleanField(default=False)
