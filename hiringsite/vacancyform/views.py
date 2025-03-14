from django.shortcuts import render
from django.views.generic import CreateView

from .models import Vacancy


def vacancy_detail(request, vacancy_id):

    _vacancy = Vacancy.objects.filter(vacancy_id=vacancy_id)


    return render(request, 'html/vacancy_detail.html', {
        "vacancy":_vacancy[0],
    })