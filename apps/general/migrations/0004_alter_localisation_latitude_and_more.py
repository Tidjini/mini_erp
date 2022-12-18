# Generated by Django 4.1.4 on 2022-12-18 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("general", "0003_localisation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="localisation",
            name="latitude",
            field=models.DecimalField(decimal_places=20, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name="localisation",
            name="longitude",
            field=models.DecimalField(decimal_places=20, max_digits=50, null=True),
        ),
    ]