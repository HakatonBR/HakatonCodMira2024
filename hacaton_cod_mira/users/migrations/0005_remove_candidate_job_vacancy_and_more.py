# Generated by Django 4.2.6 on 2024-06-01 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_candidate_phone_number_candidate_vacancy"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="candidate",
            name="job_vacancy",
        ),
        migrations.RemoveField(
            model_name="competention",
            name="competention_experience",
        ),
        migrations.DeleteModel(
            name="JobVacancy",
        ),
    ]
