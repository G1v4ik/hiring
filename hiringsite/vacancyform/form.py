from django import forms

from .models import Vacancy


class AddVacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = [
            'title',
            'company',
            'city',
            'salary',
            'employment',
            'work_schedule',
            'work_hours',
            'work_format',
            'show',
            'other'
        ]
