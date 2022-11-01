from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'password', 'bio']
    fields = ['username', 'password', 'bio']


admin.site.register(User, UserAdmin)
