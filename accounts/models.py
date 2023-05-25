from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=20, null=True)
    profile = models.TextField(max_length=100, null=True)
    profile_img = models.TextField(max_length=20, null=True)