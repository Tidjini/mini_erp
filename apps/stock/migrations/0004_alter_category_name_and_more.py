# Generated by Django 4.1.4 on 2022-12-11 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock", "0003_rename_unite_unite_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name="subcategory",
            unique_together={("name", "category")},
        ),
    ]