# Generated by Django 4.1.4 on 2022-12-18 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("general", "0002_profile"),
        ("tasks", "0002_task_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="creator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="created_tasks",
                to="general.profile",
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="receiver",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="tasks",
                to="general.profile",
            ),
        ),
    ]