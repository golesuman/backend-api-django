from django.contrib import admin
from ecommerce.models.cart import Cart, CartItem
from ecommerce.models.product import Product, Category, WishList
from ecommerce.models.order import Order, OrderItem

# Register your models here.
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Category)
admin.site.register(WishList)
