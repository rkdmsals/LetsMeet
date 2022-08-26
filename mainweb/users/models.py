from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # username = models.CharField(max_length=100, unique=True, null=False)
    # name = models.CharField(max_length=100)
    # email = models.EmailField(max_length=255,unique=True)

    nickname = models.CharField(max_length=100)
    first_name = None
    last_name = None
    

"""
class UserManager(BaseUserManager):

    use_in_migrations = True    ##수정

    def create_user(self, username, name, nickname, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username = username,
            name = name,
            nickname = nickname,
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, name, nickname, email, password=None):
        user = self.create_user(
            username = username,
            email = self.normalize_email(email),
            name = name,
            nickname = nickname,                   
            password=password
        )

        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.level = 0

        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True, null=False)
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    email = models.EmailField(max_length=255,unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email','name','nickname']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.is_admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.is_active
"""