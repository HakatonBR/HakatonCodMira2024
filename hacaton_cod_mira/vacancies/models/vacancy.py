from django.db import models

from users.models.competention import Competention


class Vacancy(models.Model):
    vacancy_id = models.AutoField(primary_key=True, unique=True)
    vacancy_name = models.CharField(max_length=125, null=False)
    vacancy_text = models.TextField(null=False)
    competention = models.ManyToManyField(Competention, related_name='vacancies', blank=True)
