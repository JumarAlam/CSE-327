from django import forms

''' inherit complaintForm from 
    generating form 
    '''

class ComplaintForm(forms.Form): 
    fullname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':"form-control"}),label='Full Name')
    email = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':"form-control"}),label='Email Address')
    comment = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class':"form-control"}), label='Comment')

