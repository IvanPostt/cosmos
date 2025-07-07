from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    photo = models.ImageField(upload_to='users/', blank=True, null=True)
    city = models.CharField(blank=True, null=True, max_length=290)
