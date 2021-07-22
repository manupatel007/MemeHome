from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User1, Tasks
# Register your models here.

class User1Admin(UserAdmin):
    pass

admin.site.register(User1, User1Admin)
admin.site.register(Tasks)
