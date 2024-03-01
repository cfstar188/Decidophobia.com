from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework import status

from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from shopping_list.serializers import ShoppingListSerializer, ChangeQuantitySerializer
from shopping_list.models import ShoppingListItem
from core.utils import get_item
from django.views.generic.edit import DeleteView

# Create your views here.
class ShoppingListView(ListAPIView):
    serializer_class = ShoppingListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ShoppingListItem.objects.filter(user=user)

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


class AddShoppingItemView(CreateAPIView):
    serializer_class = ShoppingListSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print("USER!!!!!" + request.user + '\n\n')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item_data = self.perform_create(serializer)
        return Response({
            'message': 'Product has been added to your shopping cart.',
            'item': item_data
        }, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        return serializer.save()


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

class ChangeQuantityView(UpdateAPIView):
    serializer_class = ChangeQuantitySerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_item(ShoppingListItem, self.request)
