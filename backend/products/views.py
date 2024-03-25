from rest_framework.generics import CreateAPIView
from products.permissions import ProductPermissions
from products.serializers import ProductSerializer

# Create your views here.
class CreateProductView(CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [ProductPermissions]
