from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('superuser', 'Superuser'),
        ('manager', 'Manager'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return f"{self.username} ({self.role})"
