from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('add_note', AddNote.as_view(), name='add_note'),
    path('my_notes', MyNotes.as_view(), name='my_notes'),
    path('login', UserLogin.as_view(), name='login'),
    path('registration', UserRegistration.as_view(), name='registration'),
    path('logout', user_logout, name='logout')
]

