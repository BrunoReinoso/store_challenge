from django.urls import path
from loja import views

from .views import productList, productDetail, ProductListAPI, ProductDetailAPI
urlpatterns = [
    path('', views.productList, name='productList'),
    path('product/<int:pk>/', views.productDetail, name='productDetail'),
    path('productList/', ProductListAPI.as_view(), name='productListAPI'),
    path('productDetail/<int:pk>/', ProductDetailAPI.as_view(), name='productDetailAPI')
]
