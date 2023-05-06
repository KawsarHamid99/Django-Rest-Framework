# Generated by Django 4.2.1 on 2023-05-04 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=100)),
                ("roll", models.PositiveIntegerField(default=0)),
                ("dept", models.CharField(max_length=80)),
                ("location", models.CharField(max_length=100)),
            ],
        ),
    ]
