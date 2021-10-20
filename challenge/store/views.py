from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from store.models import Product
from store.serializers import ProductSerializer


def product_list(request):

    products = Product.objects.filter()
    return render(request, 'store/productList.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/productDetail.html', {'product': product})


# class ProductList(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def post(self, *args, **kwargs):
#         import ipdb; ipdb.set_trace();
#         return super().post(*args, **kwargs)

# class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


class Product(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        import ipdb; ipdb.set_trace();
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return super().create(request, *args, **kwargs)