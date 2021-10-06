from django.urls import path
from loja import views

from .views import ProductList, ProductDetail, ProductListAPI, ProductDetailAPI
urlpatterns = [
    path('', views.ProductList, name='productList'),
    path('product/<int:pk>/', views.ProductDetail, name='productDetail'),
    path('productList/', ProductListAPI.as_view(), name='productListAPI'),
    path('productDetail/<int:pk>/', ProductDetailAPI.as_view(), name='productDetailAPI')
]
