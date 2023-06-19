from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(help_text='')
    password1 = forms.CharField(label='Password', help_text='', min_length=8)
    password2 = forms.CharField(label='Password confirmation', help_text='')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
