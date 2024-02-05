from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from backend.shopping_list.serializers import ShoppingListSerializer, ChangeQuantitySerializer
from backend.shopping_list.models import ShoppingListItem
from backend.core.utils import get_item

# Create your views here.
class ShoppingListView(ListAPIView):
    serializer_class = ShoppingListSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ShoppingListItem.objects.filter(user=user)


class AddShoppingItemView(CreateAPIView):
    serializer_class = ShoppingListSerializer
    permission_classes = [IsAuthenticated]


class DeleteShoppingItem(DestroyAPIView):
    serializer_class = ShoppingListSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_item(ShoppingListItem, self.request)

    def delete(self, request, *args, **kwargs):
        item = self.get_object()
        recipe_name = item.recipeID.name
        response = 'Removed ' + str(item) + ' from list'
        self.perform_destroy(item)
        return Response({'removed_id': item.recipeID.id,
                         'removed_name': recipe_name,
                         'numServings': item.servingSize})


class ChangeQuantityView(UpdateAPIView):
    serializer_class = ChangeQuantitySerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_item(ShoppingListItem, self.request)


