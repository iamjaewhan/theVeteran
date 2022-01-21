from django.db import models
from django.utils import timezone
from accounts.models import User, Host

# Create your models here.
class Game(models.Model):
    host = models.ForeignKey('accounts.Host', on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    
