from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField


class Candidate(models.Model):
    firstname = models.CharField(max_length=20, null=False, verbose_name='Имя')
    lastname = models.CharField(max_length=20, null=False, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=20, null=True, verbose_name='Отчество')
    telephone = PhoneNumberField(verbose_name='Телефон')
    about_us = models.TextField(verbose_name='О вас')
    resume_file = models.FileField(upload_to='doc', verbose_name='Ваше резюме (.pdf)')
    sendvacancy = models.ForeignKey('Vacancy', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.patronymic}"


class EmploymentChoice(models.TextChoices):
    full = "Полная", _("Полная")
    part_time = "Частичная", _("Частичная")
    so_so = "Полная/Частичная", _("Полная/Частичная")

class Vacancy(models.Model):
    vacancy_id = models.AutoField(primary_key=True)

    owner = models.ForeignKey(User, 
                              on_delete=models.PROTECT, 
                              blank=True, 
                              null=True, 
                              editable=True)

    title = models.CharField(max_length=300, 
                             null=False)
    
    company = models.CharField(max_length=300, 
                               verbose_name="Организация / Компания",
                               null=True)

    city = models.CharField(max_length=100, 
                            verbose_name="Город",
                            null=True)

    salary = models.DecimalField(max_digits=10,
                                 decimal_places=2, 
                                 verbose_name='Оплата в месяц')

    employment = models.CharField(max_length=30, 
                                  choices=EmploymentChoice,
                                  verbose_name='Занятость')

    work_schedule = models.CharField(max_length=100, 
                                     verbose_name='График', 
                                     null=False)

    work_hours = models.CharField(max_length=100, 
                                  verbose_name='Часы работы')
    
    work_format = models.CharField(max_length=100, 
                                   verbose_name='Формат работы')
    
    show = models.BooleanField(verbose_name='Показывать вакансию', default=True)

    other = models.TextField(max_length=100000, verbose_name='Другое', blank=True)
    
    def __str__(self):
        return f"{self.vacancy_id} - {self.title}"