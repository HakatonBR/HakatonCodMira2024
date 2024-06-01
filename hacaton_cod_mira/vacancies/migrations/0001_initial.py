# Generated by Django 4.2.6 on 2024-06-01 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vacancy",
            fields=[
                (
                    "vacancy_id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("vacancy_name", models.CharField(max_length=125)),
                ("vacancy_text", models.TextField()),
            ],
        ),
    ]