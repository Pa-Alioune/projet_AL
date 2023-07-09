from django.contrib import admin
<<<<<<< HEAD
from .models import User


admin.site.register(User)
=======
from actu_polytech.models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'role')
admin.site.register(User, UserAdmin)
>>>>>>> 9c7229121b3e771fb4c76be051a34d121413f8ac
