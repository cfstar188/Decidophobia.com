from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=15, blank=True, unique=True)
    email = models.EmailField(unique=True, blank=False)
    date_joined = models.DateTimeField(default=timezone.now)
    profile_picture = models.ImageField(upload_to="users/profile_pictures", default="users/profile_pictures/default.jpg")
    full_name = models.CharField(max_length=50, blank=True)

    objects = UserManager()
    
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
