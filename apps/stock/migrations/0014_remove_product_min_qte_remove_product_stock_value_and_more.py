# Generated by Django 4.1.4 on 2022-12-13 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stock", "0013_composition_composer_alter_composition_product"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="min_qte",
        ),
        migrations.RemoveField(
            model_name="product",
            name="stock_value",
        ),
        migrations.RemoveField(
            model_name="product",
            name="supply_qte",
        ),
        migrations.RemoveField(
            model_name="product",
            name="unite_coef",
        ),
        migrations.RemoveField(
            model_name="product",
            name="unite_value",
        ),
    ]