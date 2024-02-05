# Add important and useful helper functions here.
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404

def get_item(item_model, request):
    """Returns instance of type item_model, using current user and
    product_id. Returns 404 if instance not found."""
    user = request.user
    product = request.data.get('productID')
    try:
        return get_object_or_404(item_model, user=user, product_id=product)
    except ValueError:
        raise ValidationError("RecipeID should be an integer", 400)
