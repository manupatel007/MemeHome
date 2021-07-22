from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator #for username validation
from django.contrib.auth.hashers import make_password #it will apply pbkdf2_sha256 algorithm by default
# Create your models here.

user1_valid = RegexValidator(r'^[aA].{0,}[01]$', 'Username should start with a/A and end with 0/1')

class User1(AbstractUser):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25, unique=True, validators=[user1_valid])
    created_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=200)

    #save function is overrided to store password using SHA256
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(User1,self).save(*args,**kwargs)

class Tasks(models.Model):
    #Although id will be available by default as auto-increasing Primary key but we will explicitly declare it here
    tid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(User1, on_delete = models.CASCADE)
    task_title = models.CharField(max_length=200) #minimum length validation will be done in forms
    task_description = models.CharField(max_length=2000, blank=True)
    task_pic = models.FileField(upload_to='images/', null=True, blank=True)
    create_time_stamp = models.DateTimeField(auto_now_add=True)