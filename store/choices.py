from django.db import models


class Currency(models.TextChoices):
    USD = "USD", "$"
    EUR = "EUR", "€"
    RUB = "RUB", "₽"
    KZT = "KZT", "лв"
