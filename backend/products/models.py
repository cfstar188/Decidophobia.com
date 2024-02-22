from django.db import models
from django.core.validators import MinValueValidator

from core.core_models import BaseModel

# Create your models here.
class Product(BaseModel):
    name = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2,
                                validators=[MinValueValidator(0)])
    company = models.TextField()
    preview_picture = models.ImageField(upload_to='./product_photos', null=True, blank=True)

    def __str__(self) -> str:
        name = self.name
        price = self.price

        return f'This {name} costs {price}'
    
    
