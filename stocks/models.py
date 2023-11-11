from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=25, null=False, default='paracetamol')
    quantity = models.PositiveIntegerField(null=False)
    min_stock = models.PositiveBigIntegerField(default=100)
    cost_price = models.PositiveIntegerField(default=3500)
    selling_price = models.PositiveIntegerField(default=4000)

    def __str__(self):
        return self.name

