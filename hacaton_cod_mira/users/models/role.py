from django.db import models
from django.core.validators import MinLengthValidator 


class Role(models.TextChoices):
    HR = "HR менеджер"
    RECRUITER = "Рекрутер"
    RESOURCE_MANAGER = "Ресурсный менеджер"
    CANDIDATE = "Кандидат"
