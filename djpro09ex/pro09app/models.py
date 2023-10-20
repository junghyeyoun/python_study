from django.db import models

# Create your models here.
class Friend(models.Model):
    irum = models.CharField(max_length = 10)
    juso = models.CharField(max_length = 20)
    nai = models.IntegerField()