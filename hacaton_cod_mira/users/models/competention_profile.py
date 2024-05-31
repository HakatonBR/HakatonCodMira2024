from django.db import models

from .competention import Competention


class CompetentionProfile(models.Model):
    competention_profile_id = models.AutoField(unique=True, primary_key=True)
    scorepoint_hard_skill = models.IntegerField(default=0)
    scorepoint_soft_skill = models.IntegerField(default=0)
    scorepoint_job_vacancy = models.IntegerField(default=0)
    competention = models.ForeignKey(Competention, on_delete=models.CASCADE)
