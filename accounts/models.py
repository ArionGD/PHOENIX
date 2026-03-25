from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='user')
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    
    # Static Tax Configuration
    salary_income = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    other_income = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    monthly_savings = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    expenses_json = models.TextField(default='[]')
    occupation_type = models.CharField(max_length=20, default='salary')

    @property
    def total_inflow(self):
        return self.salary_income + self.other_income

    def __str__(self):
        return f"{self.username} ({self.role})"
