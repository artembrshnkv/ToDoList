from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .forms import *

from .utils import *


def render_result(request, template_name: str):
    return render(request, template_name, context=context)


def home(request):
    return render_result(request, 'mainapp/base.html')


class AddNote(LoginRequiredMixin, BaseMixin, CreateView):
    form_class = AddNoteForm
    template_name = 'mainapp/add_note.html'
    success_url = reverse_lazy('my_notes')

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        c_def = self.same_data(**kwargs)
        return dict(list(con.items()) + list(c_def.items()))


class MyNotes(LoginRequiredMixin, BaseMixin, ListView):
    template_name = 'mainapp/my_notes.html'
    context_object_name = 'my_notes'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        c_def = self.same_data(**kwargs)
        return dict(list(con.items()) + list(c_def.items()))

    def get_queryset(self):
        return Note.objects.filter(user_id_id=self.request.user.pk)


class UserLogin(BaseMixin, LoginView):
    template_name = 'mainapp/login.html'

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        c_def = self.same_data(**kwargs)
        return dict(list(con.items()) + list(c_def.items()))


class UserRegistration(BaseMixin, CreateView):
    template_name = 'mainapp/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        c_def = self.same_data(**kwargs)
        return dict(list(con.items()) + list(c_def.items()))


class NoteUpdate(LoginRequiredMixin,BaseMixin, UpdateView):
    template_name = 'mainapp/note_update.html'
    form_class = NoteUpdate
    success_url = 'my_notes'

    def get_context_data(self, **kwargs):
        con = super().get_context_data(**kwargs)
        c_def = self.same_data(**kwargs)
        return dict(list(con.items()) + list(c_def.items()))


def user_logout(request):
    logout(request)
    return redirect('home')


