# Generated by Django 4.2.6 on 2024-05-31 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_remove_careerpoint_role_user_role_delete_role"),
    ]

    operations = [
        migrations.AddField(
            model_name="candidate",
            name="user",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]