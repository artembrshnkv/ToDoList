from django.http import HttpResponse
from django.shortcuts import render
from .utils import *


def home(request):
    return render(request, 'mainapp/base.html', context=context)


def add_note(request):
    return render(request, 'mainapp/add_note.html', context=context)


def my_notes(request):
    return render(request, 'mainapp/my_notes.html', context=context)


