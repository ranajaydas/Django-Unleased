from django.conf import settings
from django.contrib.auth import get_user, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import View, DetailView, UpdateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Profile
from .forms import UserRegisterForm
from .utils import ProfileGetObjectMixin


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


class DisableAccount(LoginRequiredMixin, View):
    success_url = settings.LOGIN_REDIRECT_URL
    template_name = 'user/user_confirm_delete.html'

    @method_decorator(csrf_protect)
    def get(self, request):
        return TemplateResponse(request, self.template_name)

    @method_decorator(csrf_protect)
    def post(self, request):
        user = get_user(request)
        user.set_unusable_password()
        user.is_active = False
        user.save()
        logout(request)
        return redirect(self.success_url)


class ProfileDetail(LoginRequiredMixin, ProfileGetObjectMixin, DetailView):
    model = Profile


class ProfileUpdate(LoginRequiredMixin, ProfileGetObjectMixin, UpdateView):
    model = Profile
    fields = ('name', 'about',)
    success_url = reverse_lazy('profile')


class PublicProfileDetail(DetailView):
    model = Profile

