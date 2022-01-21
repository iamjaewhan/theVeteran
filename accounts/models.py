from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

# Create your models here.

class User(AbstractBaseUser):
    user_id = models.CharField(max_length=50, null=False, unique=True)
    USERNAME_FIELD = 'user_id'
    
    def __str__(self):
        return self.user_id
    
    
    
class Host(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    host_id = models.CharField(max_length=30, null=False)
    location = models.CharField(max_length=70, null=False)
    intro = models.CharField(max_length=200, null=False)