from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from products.serializers import ProductSerializer

# Create your views here.
class CreateProductView(CreateAPIView):
    serializer_class = ProductSerializer
    