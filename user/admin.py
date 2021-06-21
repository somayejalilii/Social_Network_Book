from django.contrib import admin

# Register your models here.
from user.models import User


@admin.register(User)
class User_admin(admin.ModelAdmin):
    list_display = ['id', 'username']