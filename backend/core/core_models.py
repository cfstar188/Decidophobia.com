from django.contrib.auth.models import User
from django.db import models

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# class CartProduct(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image_link = models.URLField()

#     def __str__(self):
#         return self.name

# class ShoppingCart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     products = models.ManyToManyField(CartProduct)

#     def __str__(self):
#         return f"Shopping Cart for {self.user.username}"