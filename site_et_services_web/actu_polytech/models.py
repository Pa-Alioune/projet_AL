from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    role = models.CharField(max_length=50)  # Roles: 'visitor', 'editor', 'admin'
    token = models.CharField(max_length=100, blank=True, null=True)
    token_requested = models.BooleanField(default=False)

