from django.contrib import admin
from .models import Type, Price, Product


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ("amount", "currency")
    list_filter = ("currency",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "quantity", "barcode", "updated_at", "type")
    list_filter = ("type", "price__currency")
    search_fields = ("name", "barcode")
