from django.shortcuts import render

from .models import User
from django.views import generic
from django.views.generic import TemplateView
from .forms import UserRegisterForm
from django.contrib.auth import get_user_model

# Create your views here.

class WelcomeView(TemplateView):
    template_name = 'accounts/welcome.html'

class UserRegister(generic.CreateView):
    model = get_user_model()
    fields = ['user_id', 'password']
    template_name = 'accounts/join.html'
    success_url = '/'