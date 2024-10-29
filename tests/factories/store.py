import uuid
import factory
from store.choices import Currency
from store.models import Type, Price, Product


class TypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Type

    id = factory.LazyFunction(uuid.uuid4)
    name = "Toys"
    description = "Category for sort toys items."


class PriceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Price

    id = factory.LazyFunction(uuid.uuid4)
    currency = Currency.USD
    amount = 100.00


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    id = factory.LazyFunction(uuid.uuid4)
    name = "Bear"
    price = factory.SubFactory(PriceFactory)
    type = factory.SubFactory(TypeFactory)
    quantity = 10
    barcode = factory.Faker("ean13")
