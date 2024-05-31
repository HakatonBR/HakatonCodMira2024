from django.contrib import admin

from users.models.responsibilities import Responsibilities

@admin.register(Responsibilities)
class ResponsibilitiesAdmin(admin.ModelAdmin):
    list_display = ['responsibilities_id', 'about_responsibilities']
