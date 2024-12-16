from django.db import models
from django.contrib.auth.models import AbstractUser

class Cliente(AbstractUser):
    email = models.EmailField(unique=True, max_length=100)

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name',]

    def __str__(self):
        return self.email