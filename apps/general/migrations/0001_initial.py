# Generated by Django 4.1.4 on 2022-12-29 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(
                    max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("username", models.CharField(max_length=30, unique=True)),
                ("nom", models.CharField(max_length=30)),
                ("prenom", models.CharField(max_length=30)),
                ("sex", models.IntegerField(default=1)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                ("photo", models.ImageField(max_length=1024, null=True, upload_to="")),
                ("telephone", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "telephone_deux",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("date_naissance", models.DateField(blank=True, null=True)),
                (
                    "database_name",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("exercice", models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Tva",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tva", models.CharField(max_length=50, unique=True)),
                (
                    "value",
                    models.DecimalField(
                        decimal_places=3, default=0.19, max_digits=5),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Localisation",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="localisation",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(decimal_places=20,
                                        max_digits=50, null=True),
                ),
                (
                    "latitude",
                    models.DecimalField(decimal_places=20,
                                        max_digits=50, null=True),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
