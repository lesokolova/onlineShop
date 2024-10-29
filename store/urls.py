from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, PriceViewSet, TypeViewSet

router = DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"prices", PriceViewSet)
router.register(r"types", TypeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
