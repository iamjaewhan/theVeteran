from django.shortcuts import render

from .models import User
from django.views import generic
from django.views.generic import TemplateView

# Create your views here.

class WelcomeView(TemplateView):
    template_name = 'accounts/welcome.html'

class UserRegisterView(generic.CreateView):
    model = User
    fields = ['user_id', 'password']
    template_name = 'accounts/join.html'