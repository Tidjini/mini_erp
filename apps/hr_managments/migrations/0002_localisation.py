# Generated by Django 4.1.4 on 2022-12-18 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("general", "0002_profile"),
        ("hr_managments", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Localisation",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="general.profile",
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(decimal_places=20, default=0, max_digits=50),
                ),
                (
                    "latitude",
                    models.DecimalField(decimal_places=20, default=0, max_digits=50),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
