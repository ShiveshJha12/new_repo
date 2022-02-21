from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Vehicle(models.Model):
    name=models.CharField(max_length=300,default='')
    speed=models.CharField(max_length=300,default='')
    temp=models.CharField(max_length=300,default='')
    fuel_level=models.CharField(max_length=300,default='')
    engine_status=models.CharField(max_length=300,default='')
    start = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


