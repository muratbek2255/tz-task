from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import CustomUserManager


class Gender(models.Model):
    """Пол"""
    gender = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.gender


class CustomUser(AbstractUser):
    """Кастомная модель пользователя"""
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    sent_at = models.DateTimeField(auto_now_add=True)
    gender = models.ForeignKey(to=Gender, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'city']
    objects = CustomUserManager()
