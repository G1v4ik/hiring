from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

from vacancyform.models import Vacancy


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    about_us = models.TextField(verbose_name='О вас')
    resume_file = models.FileField(upload_to='doc', verbose_name='Ваше резюме (.pdf)')
    sendvacancy = models.ForeignKey(Vacancy, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
