from django.db import models


# Create your models here(DB table).

#Drinks Category DB table 
class DrinksCategory(models.Model):
    category_name=models.CharField(max_length=200)

# Drinks Db Table with Fk making many-to-one relationship each drink assign to drink category 
class Drinks(models.Model):
    #two columns/attributes
    drink=models.CharField(max_length=200)
    price=models.IntegerField(null=True)
    #fk(asociated model,setting) relatedname:instead of showing in the Db by category_id it'll show the category_name
    #The PROTECT argument prevents the deletion of the model object that is referenced. 
    category_id=models.ForeignKey(DrinksCategory,on_delete=models.PROTECT,default=None)
    

