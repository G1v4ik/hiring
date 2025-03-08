from django.shortcuts import render
from django.contrib.auth.forms import *

from .forms import RegistrationForm

def sing_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
