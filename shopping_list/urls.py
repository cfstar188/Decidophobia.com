from django.urls import path
from shopping_list.views import AddShoppingItemView, ChangeQuantityView, DeleteShoppingItem, ShoppingListView

urlpatterns = [
    path('details/', ShoppingListView.as_view()),
    path('add-product/', AddShoppingItemView.as_view()),
    path('remove-product/', DeleteShoppingItem.as_view()),
    path('change-quantity/', ChangeQuantityView.as_view()),
]
