from django.db import models

# Create your models here.
class TaskType(models.Model):
    si_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=15)
    parent_id = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE) #since it is self pointing model

    def children(self):
        return TaskType.objects.filter(parent_id=self)