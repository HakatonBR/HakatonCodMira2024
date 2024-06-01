from django.db import models
from django.core.validators import MaxValueValidator

from .competention_profile import CompetentionProfile
from .career_profile import CareerProfile
from .sex_choice import SexChoices
from .army_status import ArmyStatus
from .education import Education
from .job_vacancy import JobVacancy
from .languages import Languages
from .status import StatusChoice
from .user import User


class Candidate(models.Model):
    candidate_id = models.AutoField(unique=True, primary_key=True)
    last_name = models.CharField(max_length=80)
    first_name = models.CharField(max_length=80)
    surname = models.CharField(max_length=80)
    resume_link = models.CharField(max_length=125)
    competention_profile = models.ForeignKey(
        CompetentionProfile,
        on_delete=models.CASCADE
    )
    career_profile = models.ForeignKey(
        CareerProfile,
        on_delete=models.CASCADE
    )
    sex = models.CharField(
        choices=SexChoices.choices,
        default=SexChoices.NO_SELECTED,
        verbose_name="Пол",
        max_length=125
    )
    age = models.IntegerField(validators=[MaxValueValidator(101)])
    army_status = models.CharField(
        choices=ArmyStatus.choices,
        default=ArmyStatus.NO_SELECTED,
        verbose_name="Статус воинской службы",
        max_length=125
    )
    education = models.CharField(
        choices=Education.choices,
        default=Education.NO_SELECTED,
        verbose_name="Образование",
        max_length=125
    )
    job_vacancy = models.ForeignKey(
        JobVacancy,
        on_delete=models.CASCADE
    )
    languages = models.CharField(
        choices=Languages.choices,
        default=Languages.NO_SELCTED,
        verbose_name="Языки",
        max_length=125
    )
    status = models.CharField(
        choices=StatusChoice.choices,
        default=StatusChoice.NOT_VIEWED,
        max_length=125
    )
    comments = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')