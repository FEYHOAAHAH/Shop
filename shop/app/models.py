from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.CharField(max_length=255)
    quantity = models.IntegerField()
    category = models.CharField(max_length=255)
    application_area = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField()

    def __str__(self):
        return self.name
