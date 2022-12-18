# Generated by Django 4.1.4 on 2022-12-13 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("stock", "0012_composition"),
    ]

    operations = [
        migrations.AddField(
            model_name="composition",
            name="composer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="composed_in",
                to="stock.product",
            ),
        ),
        migrations.AlterField(
            model_name="composition",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="composed_by",
                to="stock.product",
            ),
        ),
    ]