from django.db import models


class StatusChoice(models.TextChoices):
    NOT_VIEWED = "Не просмотрено"
    UNDER_CONSIDERATION = "На рассмотрении"
    REJECTED = "Отклонено"
    CLARIFY_DATA = "Уточнить данные"
