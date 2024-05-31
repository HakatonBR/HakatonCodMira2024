from django.db import models


class Education(models.TextChoices):
    HIGHER_EDUCATION = "Высшее"
    SECONDARY_EDUCATION = "Среднее"
    INCOMPLETE_HIGHER_EDUCATION = "Неоконченное высшее"
    INCOMPLETE_SECONDARY_EDUCATION = "Неполное среднее"
    VOCATIONAL_EDUCATION = "Средне-специальное"
    NO_SELECTED = "Не выбрано"
    