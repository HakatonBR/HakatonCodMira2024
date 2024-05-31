from django.db import models


class ArmyStatus(models.TextChoices):
    SERVED = "Отслужил"
    UNFIT = "Не годен"
    SERVING_IN_THE_RESERVES = "Прохожу службу в запасе"
    MANDATORY_MILITARY_SERVICE = "Нахожусь на срочной службе"
    CONTRACTUAL_MILITARY_SERVICE = "Нахожусь на службе по контракту"
    NO_SELECTED = "Не выбрано"
    