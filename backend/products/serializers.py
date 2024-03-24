from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'company', 'preview_picture', 'url']

    def to_representation(self, instance):
            representation = super().to_representation(instance)
            representation['price'] = float(representation['price'])
            return representation

    def create(self, validated_data):
        request = self.context['request']

        name = request.data.get('name', '')
        price = request.data.get('price', '')
        company = request.data.get('company', '')
        preview_picture = request.data.get('preview_picture', '')
        url = request.data.get('url', '')

        valid_data = validated_data | {'name': name,
                                       'price': price,
                                       'company': company,
                                       'preview_picture': preview_picture,
                                       'url': url}

        return super().create(valid_data)
