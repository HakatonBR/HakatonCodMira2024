from django.db import models
from django.core.validators import MinLengthValidator 


class Role(models.Model):
    role_id = models.AutoField(editable=False, primary_key=True)
    role_name = models.CharField(
        max_length=125,
        unique=True,
        verbose_name="Имя роли",
        validators=[MinLengthValidator(5)]
    )
    about_role = models.CharField(max_length=125, verbose_name="Кратко о роли")
