from django.urls import path

from loja import views

urlpatterns = [
    path('', views.productList, name='productList'),
    path('product/<int:pk>/', views.productDetail, name='productDetail'),
]