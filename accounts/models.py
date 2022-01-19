from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class User(AbstractBaseUser):
    user_id = models.CharField(max_length=50, Null=False, unique=True)
    
    def __str__(self):
        return self.user_id