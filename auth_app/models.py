from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given edmail and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email), **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, **extra_fields):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email=email,
            password=password, **extra_fields
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email=email,
            password=password, **extra_fields
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Create your models here.
class User(AbstractUser):
    username = None     # https://docs.djangoproject.com/en/3.2/topics/db/models/#field-name-hiding-is-not-permitted
    user_id = models.AutoField(primary_key=True, editable=False)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.email
