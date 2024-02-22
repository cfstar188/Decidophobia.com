from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.db.models import Sum
from .models import ProductItem

# Create your views here.
def cart(request):
    user_products = ProductItem.objects.filter(user=request.user)
    # Pass the user's products to the template
    total_cost = user_products.aggregate(total_cost=Sum('cost'))['total_cost'] or 0
    
    # Pass the user's products and the total cost to the template
    return render(request, 'shopcart.html', {'user_products': user_products, 'total_cost': total_cost})

def remove_from_cart(request, product_id):
    product = get_object_or_404(ProductItem, pk=product_id)
    if product.user == request.user:
        product.delete()
    return redirect('cart')