from django.db import models

# Create your models here.
class Article(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    pub_date = models.DateTimeField()