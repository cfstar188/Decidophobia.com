from django.urls import path
from products.views import CreateProductView

urlpatterns = [
    path('create-product/', CreateProductView.as_view()),
]
