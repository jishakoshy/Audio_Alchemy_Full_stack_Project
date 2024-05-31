from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username =  models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def profile(self):
        profile = Profile.objects.get(user = self)

class Profile()
