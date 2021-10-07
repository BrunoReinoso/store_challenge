import pytest
from django.urls import reverse_lazy
from rest_framework.test import APIClient

from loja.tests.factories import ProductFactory

def search_word(var, word):
    return var.content.decode("utf-8").count(word)


@pytest.mark.django_db
class TestProductViewSet:
    def setup(self):
        self.client = APIClient()
        self.list_url = reverse_lazy("loja:productList")

        products = []
        number_of_products = 4

        for i in range (0,number_of_products):

            product = ProductFactory.build()
            products.append(product)

