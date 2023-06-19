from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('add_note', add_note, name='add_note'),
    path('my_notes', my_notes, name='my_notes'),
    path('login', UserLogin.as_view(), name='login'),
    path('registration', UserRegistration.as_view(), name='registration'),
    path('logout', user_logout, name='logout')
]

