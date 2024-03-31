from rest_framework import serializers
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from products.models import Product

from shopping_list.models import ShoppingListItem


class ShoppingListSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product_id.name', read_only=True)
    product_company = serializers.CharField(source='product_id.company', read_only=True)
    product_price = serializers.DecimalField(source='product_id.price', max_digits=8, decimal_places=2, read_only=True)
    preview_picture = serializers.URLField(source='product_id.preview_picture', read_only=True)
    url = serializers.URLField(source='product_id.url', read_only=True)

    class Meta:
        model = ShoppingListItem
        fields = ('product_id', 'product_name', 'product_company', 'product_price', 'quantity', 'preview_picture', 'url')

    def to_representation(self, instance):
            representation = super().to_representation(instance)
            representation['product_price'] = float(representation['product_price'])
            return representation

    def create(self, validated_data):
        request = self.context['request']
        user = get_object_or_404(get_user_model(), id=request.user.id)
        product_id = request.data.get('product_id', '')
        product = get_object_or_404(Product, id=product_id)
        if ShoppingListItem.objects.filter(user=user, product_id=product_id):
            raise ValidationError(f"Product already in shopping cart!")
    
        valid_data = validated_data | {'user': user, 'product_id': product}
        item = super().create(valid_data)

        item_data = {
            'product_id': item.product_id.id,
            'product_name': item.product_id.name,
            'product_company': item.product_id.company,
            'product_price': item.product_id.price,
            'quantity': item.quantity,
            'preview_picture': item.product_id.preview_picture,
            'url': item.product_id.url
        }

        return item_data


class ChangeQuantitySerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product_id.name', read_only=True)

    class Meta:
        model = ShoppingListItem
        fields = ('quantity', 'product_name', 'product_id')

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance
