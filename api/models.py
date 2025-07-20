from django.db import models

class Task(models.Model):
    id=models.IntegerField(primary_key=True)
    task=models.CharField(max_length=50)
    status=models.BooleanField(default=False)
