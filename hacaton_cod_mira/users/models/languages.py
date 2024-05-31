from django.db import models


class Languages(models.TextChoices):
    ENGLISH = "Английский"
    RUSSIAN = "Русский"
    BELORUSSIAN = "Белорусский"
    UKRAINE = "Украинский"
    NO_SELCTED = "Не выбрано"
