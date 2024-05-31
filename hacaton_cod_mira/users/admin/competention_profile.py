from django.contrib import admin

from users.models.competention_profile import CompetentionProfile


@admin.register(CompetentionProfile)
class CompetentionProfileAdmin(admin.ModelAdmin):
    list_display = ['competention_profile_id', 'competention']
    