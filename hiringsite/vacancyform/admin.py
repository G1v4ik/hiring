from django.contrib import admin

from .models import Vacancy, Candidate


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 
                    'salary', 
                    'employment', 
                    'work_schedule', 
                    'work_hours', 
                    'work_format')
    
    # prepopulated_fields = {"slug": ("title",)}

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'owner', None) is None:
            obj.owner = request.user
        obj.save()