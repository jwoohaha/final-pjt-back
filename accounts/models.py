from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=20, blank=True)
    profile = models.TextField(max_length=100, blank=True)
    profile_img = models.TextField(max_length=20, blank=True)