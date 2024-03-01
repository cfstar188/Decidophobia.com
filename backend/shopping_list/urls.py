from django.urls import path
from shopping_list.views import AddShoppingItemView, ChangeQuantityView, DeleteShoppingItem, ShoppingListView
from decidophobia.views import update_cart

urlpatterns = [
    path('details/', ShoppingListView.as_view(), name='shopping-list-details'),
    path('add-item/', AddShoppingItemView.as_view()),
    path('remove-item/', DeleteShoppingItem.as_view(), name='shopping-list-delete'),
    path('change-quantity/', ChangeQuantityView.as_view()),
    path('update_cart/', update_cart, name='update_cart'),
]
