from django.contrib import admin

from ecommerce.models.account import Account
from ecommerce.models.cart import Cart, CartItem
from ecommerce.models.order import Order, OrderItem
from ecommerce.models.product import Category, Product, WishList


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price")


# Register your models here.
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Category)
admin.site.register(WishList)
admin.site.register(Account)
