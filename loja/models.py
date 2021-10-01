from django.db import models

class Product(models.Model):
    
    product_type = models.CharField(max_length=50)
    product_brand = models.CharField(max_length=50)
    product_color = models.CharField(max_length=50)
    product_size = models.CharField(max_length=3)
    product_description = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=5, decimal_places=2, default = 1.99)
    product_image = models.ImageField(upload_to='loja/')
