from django.db import models


class Competention(models.Model):
    competention_id = models.AutoField(primary_key=True, unique=True)
    competention_name = models.CharField(max_length=125)
