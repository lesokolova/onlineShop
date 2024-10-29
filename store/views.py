from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Product, Price, Type
from .serializers import ProductSerializer, PriceSerializer, TypeSerializer
from .services import reduce_product_stock


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=["post"], url_path="reduce_stock/(?P<amount>[0-9]+)")
    def reduce_stock(self, request, pk=None, amount=None):
        product = self.get_object()
        amount = int(amount)
        return reduce_product_stock(product, amount)
