from django.db import models
from django.utils.translation import gettext_lazy as _

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
    title = models.CharField(max_length=300, 
                             null=False)

    salary = models.DecimalField(max_digits=10,
                                 decimal_places=2, 
                                 verbose_name='Оплата')

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
    
    other = models.TextField(max_length=100000, verbose_name='Другое')
    
