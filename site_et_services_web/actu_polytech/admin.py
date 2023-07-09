from django.contrib import admin
from actu_polytech.models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'role','token')
admin.site.register(User, UserAdmin)
