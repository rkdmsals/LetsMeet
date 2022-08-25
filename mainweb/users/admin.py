from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group


class UserAdmin(admin.ModelAdmin):
    list_display = ( 
        'name', 
        'nickname',
        )
    search_fields = ('name', 'nickname')


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)