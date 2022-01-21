from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('',  views.WelcomeView.as_view(), name='welcome'),
    path('join', views.UserRegister.as_view(), name='join'),
]
