from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Add 'role' to the list display in admin
    list_display = ['username', 'email', 'role', 'is_staff']
    # Add 'role' to the user edit pages
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    # Add 'role' to the create user page
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
