from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.utils import validators


class UserManager(BaseUserManager):
    def create_user(self, email, phone, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, password, **extra_fields):
        user = self.create_user(email, phone, password, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None
    email = models.CharField(_('email address'), unique=True)
    phone = models.CharField(_('phone number'), max_length=15, unique=True, validators=[validators.phone_validator])
    is_merchant = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'phone']

    class Meta(AbstractUser.Meta):
        app_label = 'users'
        swappable = 'AUTH_USER_MODEL'
        verbose_name = _('User')
        verbose_name_plural = _('Users')
