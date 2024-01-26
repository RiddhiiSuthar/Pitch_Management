# Generated by Django 4.2.9 on 2024-01-25 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pitch",
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
                ("name", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("turf_type", models.CharField(max_length=255)),
                ("last_maintenance_date", models.DateTimeField()),
                ("next_maintenance_date", models.DateTimeField()),
                ("current_condition", models.IntegerField()),
            ],
        ),
    ]
