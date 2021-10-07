import factory, factory.fuzzy

from loja.models import Product

sizes = ['PP','P','M','G','GG']

class ProductFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Product

    name = factory.Faker('name', max_length=50)
    brand = factory.Faker('brand', max_length=50)
    color = factory.Faker('color', max_length=50)
    size = factory.fuzzy.FuzzyChoice(sizes)
    description = factory.Faker('description', max_length=50)
    price = factory.fuzzy.FuzzyDecimal(0, 10000)