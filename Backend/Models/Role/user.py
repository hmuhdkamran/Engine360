import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models

from Handler.PasswordHandler import Hashing


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, Username, DisplayName, password=None, **extra_fields):
        if not Username:
            raise ValueError('The given username must be set')

        hash_pass, salt = Hashing().generate_password(password)

        Username = self.normalize_email(Username)
        Language = 'English'
        user = self.model(Username=Username, DisplayName=DisplayName, Language=Language,
                          Password=hash_pass, Salt=salt, Status=True)
        user.save(using=self._db)

        return user

    def create_user(self, Username, Password, DisplayName):
        return self._create_user(Username, Password, DisplayName)

    def create_superuser(self, Username, DisplayName, password, **extra_fields):
        return self._create_user(Username, DisplayName, password, **extra_fields)


class User(AbstractBaseUser, models.Model):
    UserId = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    Username = models.TextField(null=False, unique=True)
    DisplayName = models.TextField(null=False)
    Language = models.TextField(null=False)
    Password = models.TextField(null=False)
    Salt = models.TextField(null=False)
    Status = models.BooleanField(null=False)

    USERNAME_FIELD = 'Username'
    PASSWORD_FIELD = 'Password'
    REQUIRED_FIELDS = ['DisplayName']

    objects = UserManager()

    class Meta:
        db_table = '"Role"."Users"'
