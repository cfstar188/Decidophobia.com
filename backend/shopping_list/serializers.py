from rest_framework import serializers
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from models import Product

from shopping_list.models import ShoppingListItem


class ShoppingListSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product_id.name', read_only=True)

    class Meta:
        model = ShoppingListItem
        fields = ('quantity', 'product_name', 'product_id')

    def create(self, validated_data):
        request = self.context['request']
        user = get_object_or_404(get_user_model(), id=request.user.id)
        product_id = request.data.get('productID', '')
        recipe = get_object_or_404(Product, id=product_id)
        if ShoppingListItem.objects.filter(user=user, product_id=product_id):
            raise ValidationError("Recipe already in shopping list")
 
        valid_data = validated_data | {'user': user, 'product_id': recipe}
        return super().create(valid_data)


class ChangeQuantitySerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product_id.name', read_only=True)

    class Meta:
        model = ShoppingListItem
        fields = ('quantity', 'product_name', 'product_id')

    def update(self, instance, validated_data):
        instance.servingSize = validated_data.get('quantity', instance.servingSize)
        instance.save()
        return instance
