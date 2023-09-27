from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255, unique=True)
    birthday = models.DateField(null=True, blank=True)
    join_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username
