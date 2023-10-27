from django.db import models

# Create your models here.

class Producttab(models.Model):
    category = models.CharField(max_length=20)
    pname = models.CharField(max_length=20)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    
    
    def __str__(self):
        return self.title