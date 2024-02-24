"""
URL configuration for decidophobia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import questionnaire
from .views import hello_world, home, login, signup, logout, questionnaire, submit_product, cart, remove_from_cart
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login),
    path('login/register/', signup, name='signup'),
    path('logout/', logout, name='logout'),
    #For SCRUM-13 submit form
    path('questionnaire/', questionnaire, name='questionnaire'),
    path('submit_product/', submit_product, name='submit_product'),

    path('cart/', cart, name='cart'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path("table/", include("product_table.urls"), name="table_url"),
    path("", include("django_nextjs.urls")),
    path('products/', include('products.urls')),
    # path('user_accounts/', include('user_accounts.urls')),
    path('shopping_list/', include('shopping_list.urls'))
]