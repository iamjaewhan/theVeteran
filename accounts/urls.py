from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('signup-form', views.UserRegister.as_view(), name='signup-form'),
]
