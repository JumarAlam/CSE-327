from django.test import TestCase
from StudentAssistant.models import *


class StudentTestCase(TestCase):  # NusherJK

    def test_input_is_working(self):
        Student.objects.create(uni_id=8878, fullname="something",
                               email="something@gmail.com", password='1234')
        test1 = Student.objects.get(uni_id=8878)
        self.assertEqual(test1.fullname, "something")


class LostAndFoundTestCase(TestCase):  # JumarAlam

    def testWorking(self):
        LostandFound.objects.create(finders_id=1234, itemtype="id_card", loser_id="4321",
                                    finder_contact_email="abcd@gmail.com", lost_item="Lost my ID card")
        testJumar = LostandFound.objects.get(finders_id=1234)
        self.assertEqual(testJumar.loser_id, "4321")


class ComplaintTestcase(TestCase):  # shariar
    def test(self):
        ComplainBox.objects.create(
            Complaining_person="something", message="something", Complainer_email="user@test.com")
        t1 = ComplainBox.objects.get(Complainer_email="user@test.com")
        self.assertEqual(t1.Complaining_person, "something")
