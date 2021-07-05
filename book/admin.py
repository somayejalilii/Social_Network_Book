from django.contrib import admin

# Register your models here.
from book.models import Book, Author, Comment , Like

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Like)

# @admin.register(Book)
# class Book_admin(admin.ModelAdmin):
#     list_display = ['id', 'name']