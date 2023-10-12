# Generated by Django 4.2.6 on 2023-10-12 01:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Link",
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
                ("title", models.CharField(max_length=200)),
                ("link", models.CharField(max_length=300)),
                ("icon", models.CharField(max_length=300)),
                ("color", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="LinkPage",
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
                ("title", models.CharField(max_length=200)),
                ("subtitle", models.CharField(max_length=200)),
                ("profile_image", models.CharField(max_length=300)),
            ],
        ),
    ]