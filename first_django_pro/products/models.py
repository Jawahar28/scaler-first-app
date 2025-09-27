from django.db import models
from django.db.models import Q,F

# Create your models here.
# Items in the products : id, name, price, category, stock

class Category(models.Model): # TO know that this class is tied up with the database
    # name = models.CharField(max_length=255)
    name = models.CharField(max_length=255, primary_key=True) # making name as primary key



    class Meta: # Here we can provide the constraints and other options in the "Meta" class
        ordering = ('name',) # to order the categories by name
        indexes = [
            models.Index(fields=['name']),
        ] # to create an index on the name field for faster lookups
        
        # unique_together = ('name',) # to ensure that the name is unique
        
        # We don't provide a primary key field, Django will automatically create an "id" field as the primary key

class Product(models.Model):
    # Since products have a category, we need to create a foreign key relationship with the Category model
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2) # max 10 digits, 2 after decimal
    stock = models.IntegerField() # to keep track of the stock of the product

    class Meta:
        constraints = [
            models.CheckConstraint(
                check = Q(stock__gte=0), name = "stock_non_negative"
                # stock should be greater than or equal to 0 and Q is used to create a query
            )
        ]
