from django.urls import path

from ecommerce.views.cart_view import (
    CartCreateAndListAPI,
    CartRetrieveUpdateDeleteAPI,
    CartView,
)
from ecommerce.views.home_view import HomePageAPI
from ecommerce.views.order_view import OrderCreateAndListView
from ecommerce.views.product_view import (
    ProductCreateDetailUpdateDeleteAPI,
    ProductCreateListAPI,
    SearchAPI,
    WishListAPI,
    WishListCreateAPI,
    WishListRetrieveUpdateDeleteAPI,
)
from ecommerce.views.user_auth_view import RegisterView, UserProfileView

urlpatterns = [
    path("user-profile", UserProfileView.as_view(), name="user_profile"),
    path("products", HomePageAPI.as_view(), name="home_page"),
    path("register", RegisterView.as_view(), name="user_register"),
    path("carts", CartView.as_view(), name="cart_list"),
    path(
        "wishlists/<int:id>",
        WishListRetrieveUpdateDeleteAPI.as_view(),
        name="wish_list_retrieve",
    ),
    path(
        "cart/<int:product_id>", CartCreateAndListAPI.as_view(), name="cart_create_list"
    ),
    path("search", SearchAPI.as_view(), name="search"),
    path("orders", OrderCreateAndListView.as_view(), name="order"),
    path(
        "product/<int:product_id>",
        ProductCreateDetailUpdateDeleteAPI.as_view(),
        name="product_details",
    ),
    path(
        "wishlist/<int:product_id>",
        WishListCreateAPI.as_view(),
        name="wish_list_create",
    ),
    path("wishlists", WishListAPI.as_view(), name="wishlists"),
    path(
        "cart/delete/<int:cart_id>",
        CartRetrieveUpdateDeleteAPI.as_view(),
        name="cart_retrieve_update",
    ),
]
CartRetrieveUpdateDeleteAPI
