from django.db import models
from django.urls import reverse


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
