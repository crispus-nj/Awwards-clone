from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAccount

# Register your models here.
class StyleUser(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_active')
    filter_horizontal = ()
    fieldsets = ()
    list_filter = ()
    list_display_links = ('username', )
    ordering = ('-last_login', )

admin.site.register(UserAccount, StyleUser)