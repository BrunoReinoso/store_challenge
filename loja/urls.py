from django.urls import path
from loja import views

from .views import ProductAPIView

urlpatterns = [
    path('', views.productList, name='productList'),
    path('product/<int:pk>/', views.productDetail, name='productDetail'),
    path('productAPI/', ProductAPIView.as_view(), name='productAPI')
]
