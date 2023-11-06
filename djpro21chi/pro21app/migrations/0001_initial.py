# Generated by Django 5.0a1 on 2023-11-06 07:35

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Survey",
            fields=[
                ("rnum", models.AutoField(primary_key=True, serialize=False)),
                ("gender", models.CharField(blank=True, max_length=4, null=True)),
                ("age", models.IntegerField(blank=True, null=True)),
                ("co_survey", models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                "db_table": "survey",
                "managed": False,
            },
        ),
    ]
