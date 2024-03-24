from django.db import models
from django.core.validators import MinValueValidator
<<<<<<< HEAD
=======
from django.contrib.auth import get_user_model
>>>>>>> main

from core.core_models import BaseModel

# Create your models here.
class Product(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2,
                                validators=[MinValueValidator(0)])
    company = models.CharField(max_length=255, null=False, blank=True)
    preview_picture = models.URLField(max_length = 350, null=True, blank=True)

    def __str__(self) -> str:
        name = self.name
        price = self.price

        return f'This {name} costs {price}'
    
    
<<<<<<< HEAD
=======
class Purchase(models.Model):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        product = self.product
        quantity = self.quantity
        date = self.date

        return f'Product: {product}, Quantity: {quantity}, Date: {date}'
    
>>>>>>> main
