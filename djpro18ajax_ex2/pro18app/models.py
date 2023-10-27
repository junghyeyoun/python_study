from django.db import models

# Create your models here.
class Producttab(models.Model):
    category = models.CharField(max_length=50, blank=True, null=True)
    pname = models.CharField(max_length=50, blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)
    stock = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producttab'