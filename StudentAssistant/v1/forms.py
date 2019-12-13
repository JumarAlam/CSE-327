class gradeForm(forms.Form):

    c = [('1','A'),('2','A-'),('3','B+'),('4','B'),('5','B-'),('6','C+'),('7','C'),('8','C-'),('10','D+'),('9','D') ]
    courseName = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'type':'text','class':"form-control",'placeholder':'Course Name'}), label='Course')
    courseGrade = forms.ChoiceField(choices=c,label='Grades',widget=forms.Select(attrs={'class':"form-control",'placeholder':'Course Grade'}))
    semester = forms.IntegerField(widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'Semester number'}), label='Semester')



class lostAndFoundForm(forms.Form):
    fullName = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':"form-control"}),label='Full Name')
	itemName = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':"form-control"}),label='Item Name')
	details = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':"form-control"}),label='Details')
    contactInfo = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':"form-control"}),label='Contact Number')

