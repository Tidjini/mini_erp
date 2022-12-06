# Generated by Django 4.1.3 on 2022-12-06 09:52

import apps.application.fileds
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("commercials", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="pre_qte_stock",
            field=apps.application.fileds.AppDecimalField(default=0.0),
        ),
        migrations.AlterField(
            model_name="product",
            name="pre_value",
            field=apps.application.fileds.AppDecimalField(default=0.0),
        ),
        migrations.AlterField(
            model_name="product",
            name="qte_stock",
            field=apps.application.fileds.AppDecimalField(default=0.0),
        ),
        migrations.AlterField(
            model_name="product",
            name="value",
            field=apps.application.fileds.AppDecimalField(default=0.0),
        ),
    ]
