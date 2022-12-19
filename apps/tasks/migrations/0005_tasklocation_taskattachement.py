# Generated by Django 4.1.4 on 2022-12-18 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0004_task_backcolor_task_finished_at_task_forecolor_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="TaskLocation",
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
                (
                    "start_lat",
                    models.DecimalField(decimal_places=20, max_digits=50, null=True),
                ),
                (
                    "start_lng",
                    models.DecimalField(decimal_places=20, max_digits=50, null=True),
                ),
                (
                    "end_lat",
                    models.DecimalField(decimal_places=20, max_digits=50, null=True),
                ),
                (
                    "end_lng",
                    models.DecimalField(decimal_places=20, max_digits=50, null=True),
                ),
                ("start_address", models.TextField()),
                ("end_address", models.TextField()),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="paths",
                        to="tasks.task",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TaskAttachement",
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
                ("file", models.FileField(null=True, upload_to="")),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="task_docs",
                        to="tasks.task",
                    ),
                ),
            ],
        ),
    ]