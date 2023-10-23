from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    tel = models.CharField(max_length=50)
    gen = models.CharField(max_length=10)