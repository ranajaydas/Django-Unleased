from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # Add email field to UserCreationForm

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        disallowed = ('activate',
                      'create',
                      'disable',
                      'login',
                      'logout',
                      'password',
                      'profile',)
        if username in disallowed:
            raise ValidationError("A user with that username already exists.")
        return username

    def save(self, **kwargs):
        user = super().save(commit=False)
        user.save()
        self.save_m2m()
        Profile.objects.update_or_create(user=user, defaults={'slug': slugify(user.get_username())})
        return user
