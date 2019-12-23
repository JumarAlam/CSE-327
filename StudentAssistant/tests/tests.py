from django.test import TestCase
from .form import *


class TestLogin(TestCase):
	def __init__():
		pass

	def test_login_form(self):
		#test validation
		invalid_data = {
		'user_id' :"user"
		"password": "1234"

		}

	form = LoginForm(data=invalid_data)
	form.is_valid()
	self.AssertTrue(form.errors)


'''

    user_id = forms.IntegerField(
        widget=forms.TextInput(attrs={'type':'int', 'class': "form-control", 'placeholder': 'University ID'}),
        label="University ID")
    password = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'type': 'password', 'class': "form-control", 'placeholder': 'password'}))
'''