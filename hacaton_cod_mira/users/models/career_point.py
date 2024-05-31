from django.db import models


from .company_info import CompanyInfo
from .role import Role
from .responsibilities import Responsibilities


class CareerPoint(models.Model):
    career_point_id = models.AutoField(primary_key=True, unique=True)
    company_info = models.ForeignKey(
        CompanyInfo,
        on_delete=models.CASCADE
    )
    beginning_of_work = models.DateTimeField()
    ending_of_work = models.DateTimeField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    responsibilities = models.ForeignKey(
        Responsibilities,
        on_delete=models.CASCADE
    )
