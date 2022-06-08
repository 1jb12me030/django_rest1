import email
from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=200)
    sal=models.IntegerField()
    email=models.EmailField(max_length=200)
    addr=models.CharField(max_length=200)
