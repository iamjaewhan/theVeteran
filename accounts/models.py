from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, user_id, name, password, **extra_fields):
        if not user_id:
            raise ValueError('set the user id')
        user_id = self.normalize_username(user_id)
        user = self.model(user_id = user_id, name = name, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        print("account is created")
        return user
    
    def create_user(self, user_id, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(user_id, name, password, **extra_fields)
    
    def create_superuser(self, user_id, name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser = True')
        
        return self._create_user(user_id, name, password, **extra_fields)

class User(AbstractBaseUser):
    user_id = models.CharField(max_length=50, unique=True, verbose_name='아이디')
    name = models.CharField(max_length=20, null=False, default="player")
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'user_id'
    ojects = UserManager()
    
    def __str__(self):
        return self.user_id
    
    
class Host(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    host_id = models.CharField(max_length=30, null=False)
    location = models.CharField(max_length=70, null=False)
    intro = models.CharField(max_length=200, null=False)