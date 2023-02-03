from django.db import models

# Create your models here(DB table).
class Drinks(models.Model):
    #two columns/attributes
    drink=models.CharField(max_length=200)
    price=models.IntegerField
