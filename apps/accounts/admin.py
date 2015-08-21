from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import Group

from .models import User
from .forms import AccountUserChangeForm, AccountUserCreationForm


class UserAdmin(DjangoUserAdmin):

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (u'Personal info', {'fields': ('first_name', 'last_name')}),
        (u'Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (u'Important dates', {'fields': ('last_login', 'created_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )

    readonly_fields = ('password', 'created_at',)
    list_display = ('email',)
    list_filter = ('is_active',)
    search_fields = ('email',)
    ordering = ('email',)
    form = AccountUserChangeForm
    add_form = AccountUserCreationForm

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

# class CustomUserAdmin(UserAdmin):
#     # The forms to add and change user instances

#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference the removed 'username' field



# admin.site.register(CustomUser, CustomUserAdmin)

