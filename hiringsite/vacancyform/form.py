from django import forms

from .models import Candidate


class AddVacancyForm(forms.ModelForm):


    firstname = forms.CharField(
        label='Имя',
        max_length=100,
        
    )
    lastname = forms.CharField(
        label='Фамилия',
        max_length=100,
        
    )
    patronymic = forms.CharField(
        label='Отчество',
        max_length=100,
        
    )
    telephone = forms.IntegerField(
        label='Телефон',
        required='input_user',
    )

    about_us = forms.EmailField(
        label='Расскажите о себе:',
        max_length=1000,
    )

    resume_file = forms.FileField(
        label='Фаше резюме (.pdf)'
    )

# class VacancyUserForm(forms.ModelForm):
    
#     model = Candidate

#     fields = '__all__'