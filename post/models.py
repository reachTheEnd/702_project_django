from django.db import models
from django.contrib.auth.models import Permission, User





class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    distance = models.CharField(max_length=100)
