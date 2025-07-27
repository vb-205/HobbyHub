from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from accounts.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(
        unique=True,
    )

    username = models.CharField(
        max_length=30,
        unique=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    objects = AppUserManager()

class Profile(models.Model):
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    username = models.CharField(
        max_length=30,
    )

    bio = models.TextField(
        blank=True,
        null=True,
    )

    location = models.CharField(
        blank=True,
        null=True,
    )