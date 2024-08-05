from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email',
        'username',
        'subscription',
    ]

    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields":
("email",'subscription')}),)
    fieldsets = UserAdmin.fieldsets + ((None, {"fields":
('subscription',)}),)

admin.site.register(CustomUser, CustomUserAdmin)