from rest_framework.generics import CreateAPIView
from products.permissions import ProductPermissions
from products.serializers import ProductSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from products.models import Product

# Create your views here.
class CreateProductView(CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [ProductPermissions]

    def post(self, request, *args, **kwargs):
        if product:=Product.objects.filter(name=request.data.get('name', ''),
                                           price=request.data.get('price', ''),
                                           company=request.data.get('company', ''),
                                           preview_picture=request.data.get('preview_picture', ''),
                                           url=request.data.get('url', '')).first():
            return Response({
                'id': product.id,
                'name': product.name,
                'price': float(product.price),
                'price': product.price,
                'company': product.company,
                'preview_picture': product.preview_picture
            })

        return super().post(request, *args, **kwargs)
