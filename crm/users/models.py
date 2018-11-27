from __future__ import unicode_literals
from django.contrib.auth.base_user import BaseUserManager
from django.db import models, transaction
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)


class Roles(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):

    def _create_user(self, login, password, **extra_fields):

        if not login:
            raise ValueError('The given email must be set')
        try:
            with transaction.atomic():
                user = self.model(login=login, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, login, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(login, password, **extra_fields)

    def create_superuser(self, login, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(login, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(max_length=50, unique=True, verbose_name='Логин')
    email = models.EmailField(max_length=50, unique=True, verbose_name='Email')
    name = models.CharField(max_length=100, blank=True, verbose_name='Имя')
    surname = models.CharField(max_length=100, blank=True, verbose_name='Фамилия')
    roles = models.ForeignKey(Roles, on_delete=models.CASCADE, verbose_name='Должность', null=True)
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_of_add = models.DateTimeField(default=timezone.now, verbose_name='Дата добавления')

    objects = UserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['email']

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


# class Users(models.Model):
#     name = models.CharField(max_length=100, verbose_name='Имя')
#     surname = models.CharField(max_length=100, verbose_name='Фамилия')
#     roleid = models.ForeignKey(Roles, on_delete=models.CASCADE, verbose_name='Должность', null=True)
#     login = models.CharField(max_length=100, verbose_name='Логин')
#     password = models.CharField(max_length=8, verbose_name='Пароль')
#     email = models.CharField(max_length=100, verbose_name='Email')
#     dateofadd = models.DateTimeField(blank=True, null=True, verbose_name='Дата добавления')
#     phone = models.CharField(max_length=100, verbose_name='Телефон')