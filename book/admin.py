from django.contrib import admin

# Register your models here.
from book.models import Book


@admin.register(Book)
class Book_admin(admin.ModelAdmin):
    list_display = ['id', 'book_name']