from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from .forms import *

from .utils import *


def render_result(request, template_name: str):
    return render(request, template_name, context=context)


def home(request):
    return render_result(request, 'mainapp/base.html')


@login_required
def add_note(request):
    return render_result(request, 'mainapp/add_note.html')


class AddNote(LoginRequiredMixin, CreateView):
    form_class = AddNoteForm
    template_name = 'mainapp/add_note.html'

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['menu'] = context['menu']
        return con


# def my_notes(request):
#     return render_result(request, 'mainapp/my_notes.html')


class MyNotes(LoginRequiredMixin, ListView):
    template_name = 'mainapp/my_notes.html'
    context_object_name = 'my_notes'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        con['menu'] = context['menu']
        return con

    def get_queryset(self):
        return Note.objects.filter(user_id_id=self.request.user.pk)


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


def user_logout(request):
    logout(request)
    return redirect('home')


