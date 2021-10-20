from django.urls import path

from store import views
from store.views import Product

urlpatterns = [
    path("products/", Product.as_view({'post': 'create', 'get': 'list'}), name="products"),
    path(
        "product/<int:pk>/",
        Product.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'}),
        name="product",
    ),
    path("", views.product_list, name="product_list"),
    path(
        "productdetail/<int:pk>/", views.product_detail, name="product_detail"
    ),
]
