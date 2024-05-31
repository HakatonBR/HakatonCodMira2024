from django.db import models

from .competention import Competention


class JobVacancy(models.Model):
    job_vacancy_id = models.AutoField(primary_key=True, unique=True)
    job_text = models.TextField(null=False)
    job_title = models.CharField(max_length=55, null=False)
    competention = models.ForeignKey(Competention, on_delete=models.CASCADE)
