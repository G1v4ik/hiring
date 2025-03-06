from django.contrib import admin

from .models import Vacancy, Candidate


class CandidateInline(admin.TabularInline):
    fk_name='sendvacancy'
    model=Candidate
    verbose_name='резюме кандидата'
    verbose_name_plural='резюме'


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 
                    'salary', 
                    'employment', 
                    'work_schedule', 
                    'work_hours', 
                    'work_format')
    
    inlines = [CandidateInline, ]