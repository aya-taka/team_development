from django.contrib import admin
import accounts
from . import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm


# Register your models here.


class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = models.User


class UserAdmin(UserAdmin):
    form = UserChangeForm
    fieldsets = (
        (None, {'fields': ('username', 'password', 'mailaddress', 'themeid')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'mailaddress'),
        }),
    )
    list_display = ('username', 'mailaddress', )
    list_filter = ('username', )
    search_fields = ('username', )
    ordering = ('username', )
    filter_horizontal = ()


admin.site.register(models.User, UserAdmin)