from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account
from django.utils.translation import ugettext_lazy as _


class AccountAdmin(UserAdmin):
    list_display = ('email', 'created_at', 'updated_at', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email',)
    readonly_fields = ('id', 'created_at', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    ordering = ('email',)


admin.site.register(Account, AccountAdmin)
