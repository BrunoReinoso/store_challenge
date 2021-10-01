from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from loja import views

urlpatterns = [
    path('', views.productsList, name='productsList'),
    path('product/<int:pk>/', views.productDetail, name='productDetail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
