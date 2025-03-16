from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse

from vacancyform.models import Vacancy


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, db_index=True)
    about_you = models.TextField(verbose_name='О вас', null=True)
    # resume_file = models.FileField(upload_to='doc', verbose_name='Ваше резюме (.pdf)')
    
    def get_absolute_url(self):
        return reverse('profile', kwargs={'id': self.id})


    def __str__(self):
        return f"{self.user.username}"

class VacancyResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.PROTECT, null=True)