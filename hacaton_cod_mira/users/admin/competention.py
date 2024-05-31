from django.contrib import admin

from users.models.competention import Competention


@admin.register(Competention)
class CompetentionAdmin(admin.ModelAdmin):
    list_display = ['competention_id', 'competention_name']
