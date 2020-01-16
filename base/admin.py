from django.contrib import admin
from .models import User, Product
from django.utils.safestring import mark_safe

class ProductsAdmin(admin.ModelAdmin):
     list_display    = ['name', 'description', 'price']

admin.site.register(Product, ProductsAdmin)
