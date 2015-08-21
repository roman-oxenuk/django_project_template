# coding: utf-8
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class AccountUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(AccountUserCreationForm, self).__init__(*args, **kargs)

    class Meta:
        model = User
        fields = ('email',)


class AccountUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kwargs):
        super(AccountUserChangeForm, self).__init__(*args, **kwargs)
        self.initial['password'] = self.instance.password

    class Meta:
        model = User
        fields = ('email',)