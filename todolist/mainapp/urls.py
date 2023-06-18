from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('add_note', add_note, name='add_note'),
    path('my_notes', my_notes, name='my_notes')
]

