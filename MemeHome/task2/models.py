from django.db import models

# Create your models here.
class TaskType(models.Model):
    si_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=15)
    parent_id = models.IntegerField(null=True, blank=True)