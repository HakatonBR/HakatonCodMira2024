from django.db import models


class Responsibilities(models.Model):
    responsibilities_id = models.AutoField(primary_key=True, unique=True)
    about_responsibilities = models.TextField(null=False)
