from django.contrib import admin

from vacancies.models.vacancy import Vacancy


@admin.register(Vacancy)
class VacanciesAdmin(admin.ModelAdmin):
    list_display = ['vacancy_id', 'vacancy_name', 'vacancy_text']
