from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager):
    def create_user(self, name, nickname, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            name = name,
            nickname = nickname,
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, nickname, email, password=None):
        user = self.create_user(
            name = name,
            nickname = nickname,
            email = self.normalize_email(email),
            password = password,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    email = models.EmailField(max_length=255,unique=True,)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['nickname','email']

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
