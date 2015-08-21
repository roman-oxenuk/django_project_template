# coding: utf-8
import os
import json
from inspect import isclass

from django.utils.crypto import salted_hmac
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        email = self.normalize_email(email)
        if not email:
            raise ValueError(u'Users must have an email address.')

        user = self.model(
            email=email, is_active=True
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(u'email', max_length=255, unique=True)
    first_name = models.CharField(u'имя', max_length=255, blank=True, null=True)
    last_name = models.CharField(u'фамилия', max_length=255, blank=True, null=True)

    is_active = models.BooleanField(u'активный', default=True)
    created_at = models.DateTimeField(u'дата регистрации', auto_now_add=True)
    is_staff = models.BooleanField(u'is staff', default=False)

    objects = UserManager()

    REQUIRED_FIELDS = ['password']
    USERNAME_FIELD = 'email'

    def generate_password(self):
        base = os.urandom(30)
        password = salted_hmac(settings.SECRET_KEY, base).hexdigest()[:6]
        self.set_password(password)
        return password

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name = u'user'
        verbose_name_plural = u'users'