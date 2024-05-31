from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', ]
    list_filter = ['is_active', 'is_superuser', 'is_staff']
