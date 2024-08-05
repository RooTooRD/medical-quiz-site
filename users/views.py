from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')


class ProfileView(TemplateView):
    template_name = 'users/profile.html'

