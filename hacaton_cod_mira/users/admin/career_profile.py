from django.contrib import admin

from users.models.career_profile import CareerProfile


@admin.register(CareerProfile)
class CareerProfileAdmin(admin.ModelAdmin):
    list_display = ['career_profile_id']
