from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *

from .utils import *


def home(request):
    return render(request, 'mainapp/base.html', context=context)


@login_required
def add_note(request):
    return render(request, 'mainapp/add_note.html', context=context)


def my_notes(request):
    return render(request, 'mainapp/my_notes.html', context=context)


class UserLogin(LoginView):
    template_name = 'mainapp/login.html'

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['menu'] = context['menu']
        return con


class UserRegistration(CreateView):
    template_name = 'mainapp/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['menu'] = context['menu']
        return con
