from django.contrib import admin
from .models import ProductItem
from django.conf import settings
# Register your models here.

@admin.register(ProductItem)
class ProductItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'cost', 'user')