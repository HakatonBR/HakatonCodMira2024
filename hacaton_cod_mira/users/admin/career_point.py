from django.contrib import admin
from users.models.career_point import CareerPoint


@admin.register(CareerPoint)
class CareerPointAdmin(admin.ModelAdmin):
    list_display = ['career_point_id']
