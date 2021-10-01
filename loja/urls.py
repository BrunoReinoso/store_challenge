from django.urls import path
from loja import views

urlpatterns = [
    path('', views.productsList, name='productsList'),
    path('product/<int:pk>/', views.productDetail, name='productDetail'),
]
