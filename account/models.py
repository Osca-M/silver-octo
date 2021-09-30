import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from account.managers import CustomUserManager

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Unspecified', 'Leave Unspecified')
)


class User(AbstractUser):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
