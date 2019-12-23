from django.test import TestCase
from StudentAssistant.models import Student

class StudentTestCase(TestCase): #NusherJK
    
        

    def test_input_is_working(self):
    	Student.objects.create(uni_id=8878, fullname="something", email="something@gmail.com", password='1234')
    	test1 = Student.objects.get(uni_id=8878)
    	self.assertEqual(test1.fullname, "something")
        

class LostAndFoundTestCase(TestCase):

    def testWorking(self):
        LostandFound.objects.create(finders_id = 1234, itemtype = "id_card", loser_id = "4321", finder_contact_email = "abcd@gmail.com", lost_item = "Lost my ID card")
        testJumar = LostandFound.objects.get(finders_id = 1234)
        self.assertEqual(testJumar.loser_id, "4321")

        '''

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
        '''