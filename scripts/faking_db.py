import os
import django
import random
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from store.models import Type, Price, Product
from store.choices import Currency

fake = Faker()


def create_types(n=5):
    for _ in range(n):
        Type.objects.create(
            name=fake.word().capitalize(), description=fake.text(max_nb_chars=200)
        )


def create_prices(n=20):
    currencies = [currency[0] for currency in Currency.choices]
    for _ in range(n):
        Price.objects.create(
            currency=random.choice(currencies),
            amount=round(random.uniform(10, 1000), 2),
        )


def create_products(n=20):
    types = list(Type.objects.all())
    prices = list(Price.objects.all())

    for _ in range(n):
        product_name = fake.unique.catch_phrase()
        Product.objects.create(
            name=product_name,
            price=random.choice(prices),
            quantity=random.randint(1, 100),
            barcode=fake.unique.ean13(),
            type=random.choice(types),
        )


if __name__ == "__main__":
    create_types()
    create_prices()
    create_products()
