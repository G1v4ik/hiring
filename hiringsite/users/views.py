from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


from .forms import UserRegisterForm, UserLoginForm

def users_index(request):

    return render(request, 'html/users_index.html')


def user_profile(request):

    return render(request, 'html/user_profile.html')

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