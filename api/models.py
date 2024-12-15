from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=40)
    description = models.TextField()
    price=models.DecimalField(max_digits=5, decimal_places=2)
    quantity=models.IntegerField()
    brand=models.CharField(max_length=40)
