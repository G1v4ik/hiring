from django.contrib import admin

from .models import UserProfile, VacancyResponse

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


@admin.register(VacancyResponse)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'vacancy')
