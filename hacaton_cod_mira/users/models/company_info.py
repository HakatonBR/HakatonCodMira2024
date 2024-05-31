from django.db import models


class CompanyInfo(models.Model):
    company_info_id = models.AutoField(primary_key=True, unique=True)
    company_name = models.CharField(max_length=125)
