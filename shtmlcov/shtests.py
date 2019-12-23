from django.test import TestCase
form .forms import ComplaintForm


class TestComplainForm(TestCase):
    def test_complain_form(self):
        # test validation
    invalid_data = {
        "fullname": " user ",
        "email": "user@test.com",
        "comment": 111
    }

    form = ComplaintForm(data=invalid_data)
    form.is_valid()
    self.assertTrue(forms.errors)

    valid_data = {
        "fullname": " user ",
        "email": "user@test.com",
        "comment": 111
    }
    form = ComplaintForm(data=invalid_data)
    form.is_valid()
    self.assertFalse(forms.errors)
