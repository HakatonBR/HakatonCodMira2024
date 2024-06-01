# Generated by Django 4.2.6 on 2024-05-31 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="careerpoint",
            name="role",
        ),
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("HR менеджер", "Hr"),
                    ("Рекрутер", "Recruiter"),
                    ("Ресурсный менеджер", "Resource Manager"),
                    ("Кандидат", "Candidate"),
                ],
                default="",
                max_length=125,
            ),
        ),
        migrations.DeleteModel(
            name="Role",
        ),
    ]
