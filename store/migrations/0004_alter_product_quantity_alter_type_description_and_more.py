# Generated by Django 5.1.2 on 2024-10-29 14:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0003_alter_product_quantity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="quantity",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="type",
            name="description",
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name="type",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
