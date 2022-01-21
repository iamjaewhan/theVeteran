from django.urls import path
from . import views
from .views import WelcomeView

app_name = 'accounts'


urlpatterns = [
    path('',  WelcomeView.as_view(), name='welcome')
]
