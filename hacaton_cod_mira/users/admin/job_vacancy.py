from django.contrib import admin

from users.models.job_vacancy import JobVacancy


@admin.register(JobVacancy)
class JobVacancyAdmin(admin.ModelAdmin):
    list_display = ['job_vacancy_id', 'job_text']
