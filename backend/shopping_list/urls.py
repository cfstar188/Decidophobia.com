from django.urls import path
<<<<<<< HEAD
from shopping_list.views import AddShoppingItemView, ChangeQuantityView, DeleteShoppingItem, ShoppingListView
=======
from shopping_list.views import AddShoppingItemView, ChangeQuantityView, DeleteShoppingItem, ShoppingListView, UpdatePurchases
>>>>>>> main

urlpatterns = [
    path('details/', ShoppingListView.as_view(), name='shopping-list-details'),
    path('add-item/', AddShoppingItemView.as_view()),
    path('remove-item/', DeleteShoppingItem.as_view(), name='shopping-list-delete'),
    path('change-quantity/', ChangeQuantityView.as_view()),
<<<<<<< HEAD
=======
    path('update-purchases/', UpdatePurchases.as_view())
>>>>>>> main
]
