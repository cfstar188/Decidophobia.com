# Add important and useful helper functions here.

import random
import string
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404

from products.models import Purchase

def get_item(item_model, request):
    """Returns instance of type item_model, using current user and
    product_id. Returns 404 if instance not found."""
    user = request.user
    product = request.data.get('product_id')
    try:
        return get_object_or_404(item_model, user=user, product_id=product)
    except ValueError:
        raise ValidationError("ProductID should be an integer", 400)


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    """Helper function to generate a random string of fixed length."""
    return ''.join(random.choice(chars) for _ in range(size))


def unique_order_id_generator():
    """Generates a unique order id for a purchase instance."""
    order_new_id= random_string_generator()

    qs_exists= Purchase.objects.filter(order_id= order_new_id).exists()
    if qs_exists:
        return unique_order_id_generator()
    return order_new_id
