from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    class Meta:
        db_table = 'category'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #image = models.ImageField(upload_to='products/', blank=True, null=True)

    class Meta:
        db_table = 'product'