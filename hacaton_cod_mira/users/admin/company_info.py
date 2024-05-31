from django.contrib import admin

from users.models.company_info import CompanyInfo


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['company_info_id', 'company_name']
