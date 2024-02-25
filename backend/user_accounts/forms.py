"""
USER ACCOUNT DJANGO TEMPLATE FROM THIS VIDEO: https://www.youtube.com/watch?v=Z3qTXmT0yoI
"""

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

"""
User creation form.
"""
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

"""
User login form.
"""
class CreateLoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())