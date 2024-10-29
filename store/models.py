from django.db import models

from store.choices import Currency


class Type(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Name")
    description = models.TextField(max_length=500, verbose_name="Description")

    def __str__(self):
        return self.name


class Price(models.Model):
    id = models.UUIDField(primary_key=True)
    currency = models.CharField(
        max_length=3, choices=Currency.choices, default=Currency.RUB
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.amount} {self.currency}"


class Product(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    barcode = models.CharField(max_length=50, unique=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
