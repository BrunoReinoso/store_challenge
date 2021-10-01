from django.urls import path

from loja import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.productList, name='productList'),
    path('product/<int:pk>/', views.productDetail, name='productDetail'),
]
=======
    path('', views.productsList, name='productsList'),
    path('product/<int:pk>/', views.productDetail, name='productDetail'),
]
>>>>>>> urls
