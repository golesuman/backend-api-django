from django.urls import path

from ecommerce.views.cart_view import CartCreateAndListAPI
from ecommerce.views.home_view import HomePageAPI
from ecommerce.views.order_view import OrderCreateAndListView
from ecommerce.views.product_view import (
    ProductCreateDetailUpdateDeleteAPI,
    ProductCreateListAPI,
    SearchAPI,
    WishListAPI,
)
from ecommerce.views.user_auth_view import RegisterView

urlpatterns = [
    path("products", HomePageAPI.as_view(), name="home_page"),
    # path("cart/", CartItemListAPI.as_view(), name="cart_list"),
    # path("orders/", OrderListAPI.as_view(), name="orders"),
    path("register", RegisterView.as_view(), name="user_register"),
    path(
        "cart/<int:product_id>", CartCreateAndListAPI.as_view(), name="cart_create_list"
    ),
    path("search", SearchAPI.as_view(), name="search"),
    path("order", OrderCreateAndListView.as_view(), name="order"),
    path(
        "product/<int:product_id>",
        ProductCreateDetailUpdateDeleteAPI.as_view(),
        name="product_details",
    ),
    path("wishlist/<int:product_id", WishListAPI.as_view(), name="wish_list"),
]
