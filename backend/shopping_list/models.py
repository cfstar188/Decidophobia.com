from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

from core.core_models import BaseModel
from products.models import Product

# Create your models here.
class ShoppingListItem(BaseModel):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    product_id = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1),
                                                       MaxValueValidator(100)])

    def __str__(self):
        product_name = self.product_id.name
        product_price = self.product_id.price
        return f'{product_name}: ${product_price * self.quantity}'
