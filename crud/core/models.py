from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.IntegerField(max_length=30)