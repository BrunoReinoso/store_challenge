import factory
import pytest
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APIClient

from loja.models import Product
from loja.tests.factories import ProductFactory


@pytest.mark.django_db
class TestProductViewSet:
    def setup(self):
        self.client = APIClient()
        self.list_url = reverse_lazy("loja:productListAPI")

        sequence = factory.Sequence(lambda n: n + 1)
        products = [
            ('camisa', 'nike', 'azul', 'pp', 'description 1', '1.99'),
            ('short', 'adidas', 'preta', 'g', 'descripion 2', '43.23'),
            ('blusa', 'ous', 'rosa', 'm', 'description 3', '88.00'),
        ]

        for product in products:
            ProductFactory(
                id=sequence,
                name=product[0],
                brand=product[1],
                color=product[2],
                size=product[3],
                description=product[4],
                price=product[5],
            )

    def test_get_products(self):
        response = self.client.get(self.list_url, format='json')

        assert len(response.json()) == Product.objects.count()
        assert response.status_code == status.HTTP_200_OK

    def test_confirm_first_product(self):
        product = Product.objects.filter().first()

        detail_url = reverse_lazy(
            'loja:productDetailAPI', kwargs={'pk': product.pk}
        )

        response = self.client.get(detail_url, format='json')

        assert response.json()['name'] == product.name
        assert response.json()['brand'] == product.brand
        assert response.json()['color'] == product.color
        assert response.json()['size'] == product.size
        assert response.json()['description'] == product.description
        assert response.json()['price'] == str(product.price)
        assert response.status_code == status.HTTP_200_OK
