# Generated by Django 4.1.4 on 2022-12-18 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0003_alter_task_creator_alter_task_receiver"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="backcolor",
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="task",
            name="finished_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="task",
            name="forecolor",
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="statue",
            field=models.CharField(
                choices=[
                    ("i", "instance"),
                    ("a", "accepted"),
                    ("p", "in progress"),
                    ("t", "terminated"),
                    ("c", "canceled"),
                ],
                default="i",
                max_length=1,
            ),
        ),
    ]
