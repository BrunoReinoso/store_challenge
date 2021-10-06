from django.shortcuts import get_object_or_404, render

from loja.models import Product
from loja.serializers import ProductSerializer

from rest_framework.views import APIView , Response

# Create your views here.


def productList(request):

    products = Product.objects.filter()
    return render(request, 'loja/productList.html', {'products': products})

def productDetail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'loja/productDetail.html', {'product': product})

class ProductAPIView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)