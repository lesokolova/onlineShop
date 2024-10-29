from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product, Price, Type
from .serializers import ProductSerializer, PriceSerializer, TypeSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=["post"])
    def reduce_stock(self, request, pk=None):
        product = self.get_object()
        amount = request.data.get("amount", 0)

        try:
            amount = int(amount)
            if amount <= 0:
                return Response(
                    {"error": "Amount should be a positive integer."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if product.quantity < amount:
                return Response(
                    {"error": "Not enough stock available."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            product.quantity -= amount
            product.save()
            return Response(
                {
                    "message": f"Stock reduced by {amount}. Remaining stock: {product.quantity}"
                },
                status=status.HTTP_200_OK,
            )

        except ValueError:
            return Response(
                {"error": "Invalid amount value."}, status=status.HTTP_400_BAD_REQUEST
            )
