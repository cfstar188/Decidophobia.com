from django.shortcuts import render, get_object_or_404
from rest_framework import status
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from shopping_list.serializers import ShoppingListSerializer, ChangeQuantitySerializer
from shopping_list.models import ShoppingListItem
from products.models import Product, Purchase
from core.utils import get_item, unique_order_id_generator

# Create your views here.
class ShoppingListView(ListAPIView):
    serializer_class = ShoppingListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ShoppingListItem.objects.filter(user=user)


class AddShoppingItemView(CreateAPIView):
    serializer_class = ShoppingListSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print("USER!!!!!" + request.user + '\n\n')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item_data = self.perform_create(serializer)
        print(item_data)
        return Response({
            'message': 'Product has been added to your shopping cart.',
            'item': item_data
        }, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        return serializer.save()


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


class ChangeQuantityView(UpdateAPIView):
    serializer_class = ChangeQuantitySerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_item(ShoppingListItem, self.request)


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
            order_id = unique_order_id_generator().upper()
            Purchase.objects.create(user=user,
                                    product=product,
                                    quantity=list_item.quantity,
                                    order_id=order_id)

        for item in successfully_removed:
            item.delete()
        return Response({'message': 'Purchase history updated!'}, status=status.HTTP_200_OK)
