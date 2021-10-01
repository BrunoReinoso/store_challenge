from django.db import models

class Product(models.Model):
    
    productType = models.CharField(max_length=50)
    productBrand = models.CharField(max_length=50)
    productColor = models.CharField(max_length=50)
    productSize = models.CharField(max_length=3)
    productDescription = models.CharField(max_length=100)
    productPrice = models.DecimalField(max_digits=5, decimal_places=2, default = 1.99)
    productImage = models.ImageField(upload_to='loja/')
