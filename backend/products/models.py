from django.db import models
from django.core.validators import MinValueValidator

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
    
    
