from django.contrib import admin

from users.models import User

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

class UserAdmin(BaseUserAdmin):

    list_display = (
        'username',
        'email',
        'is_active',
        'is_staff',
        'phone_number'
    )

    search_fields = (
        'username',
        'email'
    )

    list_display_links = None

    readonly_fields = ('username','first_name','last_name','email')


admin.site.register(User,UserAdmin)

# Register your models here.
