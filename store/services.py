from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from .models import Product


def reduce_product_stock(product: Product, amount: int):
    """
    Reduce the stock of the given product by the specified amount.
    """
    try:
        if amount <= 0:
            raise ValidationError("Amount should be a positive integer.")

        if product.quantity < amount:
            raise ValidationError("Not enough stock available.")

        product.quantity -= amount
        product.save()

        return Response(
            {
                "message": f"Stock reduced by {amount}. Remaining stock: {product.quantity}"
            },
            status=status.HTTP_200_OK,
        )
    except ValidationError as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
