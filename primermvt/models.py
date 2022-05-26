from datetime import datetime
from django.db import models


# Create your models here.

class primermvt(models.Model):
    name = models.CharField(max_length=50)
    edad = models.IntegerField()
    nacimiento = models.CharField(max_length=10)
    active = models.BooleanField(default = True)