from django.shortcuts import get_object_or_404, render
from rest_framework import generics

from store.models import Product
from store.serializers import ProductSerializer

# Create your views here.


def ProductList(request):

    products = Product.objects.filter()
    return render(request, 'store/productList.html', {'products': products})


def ProductDetail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/productDetail.html', {'product': product})


class ProductListAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
