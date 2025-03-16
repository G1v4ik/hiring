from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.db import transaction

from .forms import UserRegisterForm, UserLoginForm, ProfileUpdateForm
from .models import UserProfile

def users_index(request):

    return render(request, 'html/users_index.html')


def user_profile(request, id):
    user = request.user
    user_isauth = user.is_authenticated
    profile = UserProfile.objects.filter(user=user)

    if profile.exists():
        ...
    else:
        UserProfile.objects.create(user=user, about_you=None).save()

    return render(request, 'html/user_profile.html', {
        'user_isauth': user_isauth,
        'user':user,
        'profile':profile[0]

    })

class UserRegister(SuccessMessageMixin, CreateView):

    form_class = UserRegisterForm
    success_url = reverse_lazy('home')
    template_name = 'html/user_register.html'
    success_message = 'Успешная регистрация'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация на сайте'
        return context
    

class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'html/user_login.html'
    next_page = reverse_lazy('home')
    success_message = 'Добро пожаловать на сайт!'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация на сайте'
        return context


class UserLogoutView(LogoutView):

    next_page = reverse_lazy('user')


class ProfileUpdateView(UpdateView):
    model = UserProfile
    fields = ["about_you"]
    template_name = 'html/user_update.html'
    success_message = 'Успешно'

    def get_object(self, queryset=None):
        obj = UserProfile.objects.get(user_id=self.kwargs['pk'])
        return obj
