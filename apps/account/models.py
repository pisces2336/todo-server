from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from core.models import BaseModel


class UserManager(BaseUserManager):
    pass


class User(BaseModel, AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    last_login = None

    USERNAME_FIELD = "email"

    objects = UserManager

    class Meta:
        db_table = "user"
