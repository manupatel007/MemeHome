from django import forms
from django.forms import CharField,ModelForm
from .models import User1, Tasks
from django.contrib.auth.password_validation import validate_password

class UserForm(ModelForm):
    password = CharField(widget=forms.PasswordInput(), validators=[validate_password]) #basic password validation by django applied
    class Meta:
        model = User1
        exclude = ['created_at']

class TasksForm(ModelForm):
    task_title = CharField(min_length=10, max_length=200) #Minimum length constraint applied
    class Meta:
        model = Tasks
        fields = '__all__'