import factory

from store.models import Product

sizes = ['PP', 'P', 'M', 'G', 'GG']


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = 'name'
    brand = 'brand'
    color = 'color'
    size = 'PP'
    description = 'description'
    price = '1.99'
