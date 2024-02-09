from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import admin



# Create your models here.


class ProductItem(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.name