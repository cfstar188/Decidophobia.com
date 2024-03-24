from django.urls import path
from shopping_list.views import AddShoppingItemView, ChangeQuantityView, DeleteShoppingItem, ShoppingListView, UpdatePurchases

urlpatterns = [
    path('details/', ShoppingListView.as_view(), name='shopping-list-details'),
    path('add-item/', AddShoppingItemView.as_view()),
    path('remove-item/', DeleteShoppingItem.as_view(), name='shopping-list-delete'),
    path('change-quantity/', ChangeQuantityView.as_view()),
    path('update-purchases/', UpdatePurchases.as_view())
]
