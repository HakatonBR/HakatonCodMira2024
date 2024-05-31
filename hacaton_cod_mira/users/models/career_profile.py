from django.db import models

from .career_point import CareerPoint


class CareerProfile(models.Model):
    career_profile_id = models.AutoField(primary_key=True, unique=True)
    experience = models.IntegerField()
    scorepoint_job_vacancy = models.IntegerField()
    career_point = models.ForeignKey(
        CareerPoint,
        on_delete=models.CASCADE
    )
