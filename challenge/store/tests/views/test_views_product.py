import factory
import pytest
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APIClient

from store.models import Product
from store.tests.factories import ProductFactory


@pytest.mark.django_db
class TestProductViewSet:
    def setup(self):
        self.client = APIClient()
        self.list_url = reverse_lazy("store:products")

        ProductFactory.reset_sequence()
        sequence = factory.Sequence(lambda n: n + 1)
        products = [
            ('camisa', 'nike', 'azul', 'pp', 'description 1', 1.99),
            ('short', 'adidas', 'preta', 'g', 'descripion 2', 43.23),
            ('blusa', 'ous', 'rosa', 'm', 'description 3', 88.00),
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

    def test_confirm_product_detail(self):
        product = Product.objects.get(pk=1)

        detail_url = reverse_lazy('store:product', kwargs={'pk': product.pk})

        response = self.client.get(detail_url, format='json')

        assert response.json()['name'] == product.name
        assert response.json()['brand'] == product.brand
        assert response.json()['color'] == product.color
        assert response.json()['size'] == product.size
        assert response.json()['description'] == product.description
        assert response.json()['price'] == str(product.price)

        assert response.status_code == status.HTTP_200_OK

    def test_create_product_with_sucess(self, product_payload):
        #import ipdb; ipdb.set_trace();
        response = self.client.post(self.list_url, format='json', data=product_payload)
        
        assert response.status_code == status.HTTP_200_OK
        

    def test_can_not_find_product(self):
        detail_url = reverse_lazy('store:product', kwargs={'pk': 999})

        response = self.client.get(detail_url, format='json')

        assert response.status_code == status.HTTP_404_NOT_FOUND

# - test create product with sucess
# - create product with bad request (informações insuficientes ou payload zoado)
# - test put with sucess
# - test put 404
