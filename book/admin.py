from django.contrib import admin

# Register your models here.
from book.models import Book, Author

admin.site.register(Book)
admin.site.register(Author)

# @admin.register(Book)
# class Book_admin(admin.ModelAdmin):
#     list_display = ['id', 'name']