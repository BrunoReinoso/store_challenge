from django.urls import path

from store import views
from store.views import ProductDetail, ProductList

urlpatterns = [
    path("products/", ProductList.as_view(), name="products"),
    path(
        "product/<int:pk>/",
        ProductDetail.as_view(),
        name="product",
    ),
    path("", views.product_list, name="product_list"),
    path(
        "productdetail/<int:pk>/", views.product_detail, name="product_detail"
    ),
]
