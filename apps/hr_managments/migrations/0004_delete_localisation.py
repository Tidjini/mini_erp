# Generated by Django 4.1.4 on 2022-12-18 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hr_managments", "0003_alter_employe_type"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Localisation",
        ),
    ]
