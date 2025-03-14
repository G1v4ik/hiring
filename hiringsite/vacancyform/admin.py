from django.contrib import admin
from django.shortcuts import render, HttpResponseRedirect
from django.utils.html import format_html
from django.urls import path

from .models import Vacancy, EmploymentChoice

from faker import Faker

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 
                    'salary', 
                    'employment', 
                    'work_schedule', 
                    'work_hours', 
                    'work_format')
    
    # prepopulated_fields = {"slug": ("title",)}

    change_list_template = 'html/admin/change_admin.html'

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'owner', None) is None:
            obj.owner = request.user
        obj.save()
    

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('fake_info/', self.fake_info),
        ]
        return my_urls + urls
    
    
    def fake_info(self, request):
        fake = Faker()
        Vacancy.objects.create(
            owner = request.user,
            title = fake.text(max_nb_chars=50),
            company = fake.text(max_nb_chars=50),
            city = fake.city(),
            salary = fake.random_number(digits=5),
            employment = EmploymentChoice.full,
            work_schedule = fake.text(max_nb_chars=50),
            work_hours = fake.text(max_nb_chars=50),
            work_format = fake.text(max_nb_chars=50),
            show = True,
            other = fake.text(max_nb_chars=500),
        )

        return HttpResponseRedirect("../")

