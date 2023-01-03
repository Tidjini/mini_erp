# Generated by Django 4.1.4 on 2023-01-02 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("general", "0003_remove_profile_autre"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="statue",
            field=models.CharField(
                choices=[
                    ("u", "undefined"),
                    ("a", "active"),
                    ("n", "non active"),
                    ("ab", "absent"),
                ],
                default="i",
                max_length=2,
            ),
        ),
    ]