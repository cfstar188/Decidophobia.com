from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model

from core.core_models import BaseModel

# Create your models here.
class Product(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2,
                                validators=[MinValueValidator(0)])
    company = models.CharField(max_length=255, null=False, blank=True)
    preview_picture = models.URLField(max_length = 350, null=True, blank=True)
    url = models.URLField(max_length = 350, null=True, blank=True)

    def __str__(self) -> str:
        name = self.name
        price = self.price

        return f'This {name} costs {price}'
    
    
class Purchase(models.Model):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    order_id = models.CharField(max_length=150, null=False, blank=False, default='')
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        product = self.product
        quantity = self.quantity
        date = self.purchase_date

        return f'Product: {product}, Quantity: {quantity}, Date: {date}'
    