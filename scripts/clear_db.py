import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from store.models import Type, Price, Product


def clear_database():
    Product.objects.all().delete()
    Price.objects.all().delete()
    Type.objects.all().delete()


if __name__ == "__main__":
    clear_database()
