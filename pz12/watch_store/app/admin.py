from django.contrib import admin
from .models import Product, Cart, CartItem, Profile
from django.contrib.auth.admin import UserAdmin


admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Profile)
