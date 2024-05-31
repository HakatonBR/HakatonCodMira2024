from django.db import models


class SexChoices(models.TextChoices):
    MAN = "Мужской"
    WOMAN = "Женский"
    OTHER = "Другое"
    NO_SELECTED = "Не выбрано"
