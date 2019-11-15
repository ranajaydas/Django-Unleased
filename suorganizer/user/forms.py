from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()                                    # Add email field to UserCreationForm

    class Meta:
        model = User                                              # Changes the User model
        fields = ['username', 'email', 'password1', 'password2']  # The order in which the fields are shown


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()                                    # Add email field to user models

    class Meta:
        model = User
        fields = ['username', 'email']
