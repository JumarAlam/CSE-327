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
