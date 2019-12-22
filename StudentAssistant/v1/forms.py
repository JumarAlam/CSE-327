from django import forms

class LoginForm(forms.Form):
"""
	LoginForm class
	Attributes: user_id, password
	This class takes the user_id and password from frontend form and pass them to models
"""
    user_id = forms.IntegerField(
        widget=forms.TextInput(attrs={'type':'int', 'class': "form-control", 'placeholder': 'University ID'}),
        label="University ID")
    password = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'type': 'password', 'class': "form-control", 'placeholder': 'password'}))


class gradeForm(forms.Form):
"""
	GradeForm class
	Attributes: courseName, courseGrade, semester
	This class takes the courseName, courseGrade and semester from frontend form. After calculating the grades in models it passes the data to database.
"""
    c = [('1','A'),('2','A-'),('3','B+'),('4','B'),('5','B-'),('6','C+'),('7','C'),('8','C-'),('10','D+'),('9','D') ]
    courseName = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'type':'text','class':"form-control",'placeholder':'Course Name'}), label='Course')
    courseGrade = forms.ChoiceField(choices=c,label='Grades',widget=forms.Select(attrs={'class':"form-control",'placeholder':'Course Grade'}))
    semester = forms.IntegerField(widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'Semester number'}), label='Semester')




class LostForm(forms.Form):
"""
	LostForm class
	Attributes: item, itemtype, loser_id, description, contactInfo
	This class takes the citem, itemtype, loser_id, description and contactInfo from frontend form.
"""
    item = [('1', 'ID_Card'), ('2', 'Pen-Drive'), ('3','others')]
    itemtype = forms.ChoiceField(choices=item, label='Item' ,widget=forms.Select(attrs={'class':"form-control",'placeholder':'Item'}))
    loser_name = forms.CharField( label='Name(if available)' ,widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'Name'}))
    loser_id = forms.CharField( label='Id(if available)' ,widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'ID'}))
    description = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class':"form-control"}), label='Comment')


class RegistrationForm(forms.Form):
    user_id = forms.IntegerField(widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'University ID'}), label="University ID")
    fullname = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'type':'text','class':"form-control",'placeholder':'Fullname'}), label="Fullname")
    email = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'type':'text','class':"form-control",'placeholder':'Email ID'}), label="Email Address")
    password = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'type':'password','class':"form-control",'placeholder':'password'}))
    confirm_password = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'type':'password','class':"form-control",'placeholder':'password'}))

class LoginForm(forms.Form):
    user_id = forms.IntegerField(
        widget=forms.TextInput(attrs={'type':'int', 'class': "form-control", 'placeholder': 'University ID'}),
        label="University ID")
    password = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'type': 'password', 'class': "form-control", 'placeholder': 'password'}))
        
        
        
        
class Evaluation(forms.Form):
    options = (('1', 'Agree'),('2', 'Neutral'), ('3','Disagree'))

    facultyname = forms.CharField(label = 'faculty name', widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'facultyname'}))
    option1 = forms.ChoiceField(choices= options,label = 'The Instructor was adequate prepared for class',  widget= forms.RadioSelect(attrs={ 'placeholder':'option1'}))
    option2 = forms.ChoiceField(choices= options,label = 'The Instructor began and ended class on time, and used class time effectively',  widget= forms.RadioSelect(attrs={'placeholder':'option2'}))
    option3 = forms.ChoiceField(choices= options,label = 'The instructor\'s teaching method was effective, adn sessions were clear and understandable.',  widget= forms.RadioSelect(attrs={'placeholder':'option3'}))
    option4 = forms.ChoiceField(choices= options,label = 'The instructor was available during office hours and was helpful.',  widget= forms.RadioSelect(attrs={'placeholder':'option4'}))
    option5 = forms.ChoiceField(choices= options,label = 'The instructor had good command over the subject matter of the course.',  widget= forms.RadioSelect(attrs={'placeholder':'option5'}))
    option6 = forms.ChoiceField(choices= options,label = 'The instructor was fair in grading exams, quizzes, assignments and provided timely feedback.',  widget= forms.RadioSelect(attrs={'placeholder':'option6'}))

    comment = forms.CharField(label= 'Comment', widget= forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Extra commnets'}))