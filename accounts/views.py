from django.shortcuts import render

from .models import User
from django.views import generic
from django.views.generic import TemplateView, CreateView
from .forms import UserForm
from django.contrib.auth import get_user_model

# Create your views here.

class WelcomeView(TemplateView):
    template_name = 'accounts/welcome.html'

class UserRegister(CreateView):
    form_class = UserForm
    template_name = 'accounts/signup.html'
    success_url = '/'