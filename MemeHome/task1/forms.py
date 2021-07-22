from django import forms
from django.forms import CharField,ModelForm,Textarea
from .models import User1, Tasks
from django.contrib.auth.password_validation import validate_password

class UserForm(ModelForm):
    password = CharField(widget=forms.PasswordInput(), validators=[validate_password]) #basic password validation by django applied
    class Meta:
        model = User1
        fields = ['username','password']

class TasksForm(ModelForm):
    task_title = CharField(min_length=10, max_length=200) #Minimum length constraint applied
    class Meta:
        model = Tasks
        exclude = ['uid']
        widgets = {
            'task_description': Textarea(attrs={'cols': 80, 'rows': 5}),
        }