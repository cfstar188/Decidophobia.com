from django.db import models
# Create your models here.
from django.db import connection
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    productId = models.PositiveIntegerField(primary_key=True)
    productName = models.CharField(max_length=50)
    price = models.FloatField(validators=[MinValueValidator(0)])
    customerReview = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    SHIPPING_TIME_CHOICES = [
        ('Doesn\'t matter', 'Doesn\'t matter'),
        ('A couple weeks', 'A couple weeks'),
        ('A week or so', 'A week or so'),
        ('Amazon speed', 'Amazon speed'),
        ('Right now', 'Right now'),
    ]
    shippingTime = models.CharField(max_length=50, choices=SHIPPING_TIME_CHOICES)
    RETURN_POLICY_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    returnPolicy = models.CharField(max_length=3, choices=RETURN_POLICY_CHOICES)
    BRAND_REPUTATION_CHOICES = [
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Ok', 'Ok'),
    ]
    brandReputation = models.CharField(max_length=10, choices=BRAND_REPUTATION_CHOICES)

    def __str__(self):
        return self.productName

# Product.objects.using('test_database').all()