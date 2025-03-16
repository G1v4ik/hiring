from django.shortcuts import render, redirect
from django.views.generic import RedirectView
from django.views.generic.edit import UpdateView, CreateView, \
DeleteView

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from .models import Vacancy
from .form import AddVacancyForm


def vacancy_detail(request, vacancy_id):

    _vacancy = Vacancy.objects.filter(vacancy_id=vacancy_id)


    return render(request, 'html/vacancy_detail.html', {
        "vacancy":_vacancy[0],
    })


def get_my_vacancy(request):
    vacancy_user = Vacancy.objects.filter(owner=request.user)

    return render(request, 'html/vacancy_my.html', {
        "vacancy_user": vacancy_user,
    })


class VacancyResponse(RedirectView):


    def get_redirect_url(self, *args, **kwargs):
        url_redirect = reverse_lazy('home')

        

        return url_redirect


class VacancyCreateView(PermissionRequiredMixin, CreateView):
    # model = Vacancy
    form_class = AddVacancyForm
    template_name = 'html/vacancy_create.html'
    permission_required = ('vacancyform.add')
    raise_exception = True

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.owner = self.request.user
        return super().form_valid(form)


class VacancyDeleteView(DeleteView):
    model = Vacancy
    success_url = reverse_lazy('vacancy_my')

    

