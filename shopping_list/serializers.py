from rest_framework import serializers
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
# from scrum_13_questionnaire.models import Product

from shopping_list.models import ShoppingListItem


class ShoppingListSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product_id.name', read_only=True)

    class Meta:
        model = ShoppingListItem
        fields = ('quantity', 'product_name', 'product_id')

    def create(self, validated_data):
        print("Adding item")
        request = self.context['request']
        user = get_object_or_404(get_user_model(), id=request.user.id)
        product_id = request.data.get('productID', '')
        product = get_object_or_404(ShoppingListItem, id=product_id)
        if ShoppingListItem.objects.filter(user=user, product_id=product_id):
            raise ValidationError("Product already in shopping cart!")
 
        valid_data = validated_data | {'user': user, 'product_id': product}
        return super().create(valid_data)


class ChangeQuantitySerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product_id.name', read_only=True)

    class Meta:
        model = ShoppingListItem
        fields = ('quantity', 'product_name', 'product_id')

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance
