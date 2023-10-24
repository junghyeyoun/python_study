# Generated by Django 5.0a1 on 2023-10-24 15:35

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BoardTab",
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
                ("name", models.CharField(max_length=20)),
                ("passwd", models.CharField(max_length=20)),
                ("mail", models.CharField(max_length=30)),
                ("title", models.CharField(max_length=100)),
                ("cont", models.TextField()),
                ("bip", models.GenericIPAddressField()),
                ("bdate", models.DateTimeField()),
                ("readcnt", models.IntegerField()),
                ("gnum", models.IntegerField()),
                ("onum", models.IntegerField()),
                ("nested", models.IntegerField()),
            ],
        ),
    ]
