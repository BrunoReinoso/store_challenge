from django.shortcuts import get_object_or_404, render

from loja.models import Product

# Create your views here.


def productsList(request):

    products = Product.objects.filter()
    return render(request, 'loja/productList.html', {'products': products})


def productDetail(request, pk):

    product = get_object_or_404(Product, pk=pk)
    return render(request, 'loja/productDetail.html', {'product': product})
