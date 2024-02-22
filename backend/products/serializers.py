from rest_framework import serializers

from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        request = self.context['request']

        name = request.data.get('name', '')
        price = request.data.get('price', '')
        company = request.data.get('company', '')
        preview_picture = request.data.get('preview_picture', '')

        valid_data = validated_data | {'name': name, 'price': price, 'company': company, 'preview_picture': preview_picture}
        return super().create(valid_data)
