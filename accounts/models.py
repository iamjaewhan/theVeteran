from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, UserManager
from django.utils import timezone

# Create your models here.
class CustomUserManager(UserManager):
    def create_user(self, user_id, password=None):
        if not user_id:
            raise ValueError('create_user() missing user id')
        user = self.model(user_id=user_id)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, user_id, password):
        return self.create_user(user_id, password)

class User(AbstractBaseUser):
    user_id = models.CharField(max_length=50, unique=True, verbose_name='아이디')
    name = models.CharField(max_length=20, null=False, default="player")
    
    USERNAME_FIELD = 'user_id'
    
    def __str__(self):
        return self.user_id
    
class Host(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    host_id = models.CharField(max_length=30, null=False)
    location = models.CharField(max_length=70, null=False)
    intro = models.CharField(max_length=200, null=False)