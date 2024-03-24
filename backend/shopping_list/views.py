<<<<<<< HEAD
from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework import status

from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
=======
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
>>>>>>> main
from rest_framework.permissions import IsAuthenticated

from shopping_list.serializers import ShoppingListSerializer, ChangeQuantitySerializer
from shopping_list.models import ShoppingListItem
<<<<<<< HEAD
from core.utils import get_item
from django.views.generic.edit import DeleteView
=======
from products.models import Product, Purchase
from core.utils import get_item
>>>>>>> main

# Create your views here.
class ShoppingListView(ListAPIView):
    serializer_class = ShoppingListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ShoppingListItem.objects.filter(user=user)

<<<<<<< HEAD
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        items = []
        total_cost = 0.0
        for item in queryset:
            total_cost += float(item.product_id.price) * item.quantity
            items.append({'product_id': item.product_id.id,
                          'product_name': item.product_id.name,
                          'product_company': item.product_id.company,
                          'product_price': item.product_id.price,
                          'quantity': item.quantity})

        context = {'user_products': items, 'total_cost': total_cost}
        return render(self.request, 'shopcart.html', context=context)

=======
>>>>>>> main

class AddShoppingItemView(CreateAPIView):
    serializer_class = ShoppingListSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item_data = self.perform_create(serializer)
<<<<<<< HEAD
=======
        print(item_data)
>>>>>>> main
        return Response({
            'message': 'Product has been added to your shopping cart.',
            'item': item_data
        }, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        return serializer.save()


<<<<<<< HEAD
class DeleteShoppingItem(DeleteView):
    model = ShoppingListItem
    template_name = 'shopcart.html'
    success_url = reverse_lazy('shopping-list-details')  # replace with the name of your shopping list URL

    def get_object(self):
        product_id = self.request.POST.get('product_id', '')
        item = self.model.objects.filter(product_id=product_id)
        return item

    def delete(self, request, *args, **kwargs):
        product_id = self.request.POST.get('product_id', '')
        item = self.model.objects.filter(product_id=product_id).first()

        if item:
            item.delete()
            context = {
                'message': 'Removed item from list',
                'item': {
                    'removed_id': item.product_id.id,
                    'removed_name': item.product_id.name,
                    'quantity': item.quantity
                }
            }

            return render(request, 'shopcart.html', context)
=======
class DeleteShoppingItem(DestroyAPIView):
    serializer_class = ShoppingListSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_item(ShoppingListItem, self.request)

    def delete(self, request, *args, **kwargs):
        item = self.get_object()
        self.perform_destroy(item)

        return Response({'message': 'Removed item from list',
                         'item': {'removed_id': item.product_id.id,
                         'removed_name': item.product_id.name,
                         'quantity': item.quantity}}, status=status.HTTP_200_OK)

>>>>>>> main

class ChangeQuantityView(UpdateAPIView):
    serializer_class = ChangeQuantitySerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_item(ShoppingListItem, self.request)
<<<<<<< HEAD
=======


class UpdatePurchases(CreateAPIView):
    # serializer_class = ShoppingListSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        bought_items = request.data.get('products', [])
        print(bought_items)
        successfully_removed = []
        for item_id in bought_items:
            product = get_object_or_404(Product, id=item_id)
            list_item = get_object_or_404(ShoppingListItem, user=user, product_id=product)
            successfully_removed.append(list_item)
            Purchase.objects.create(user=user, product=product, quantity=list_item.quantity)

        for item in successfully_removed:
            item.delete()
        return Response({'message': 'Purchase history updated!'}, status=status.HTTP_200_OK)
>>>>>>> main
