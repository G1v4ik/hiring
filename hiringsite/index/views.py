from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from vacancyform.models import Vacancy


def index_view(request):
    vacancies = Vacancy.objects.all()
    paginator = Paginator(vacancies, 6)

    return render(request, 'html/index.html', {'vacancies': vacancies})