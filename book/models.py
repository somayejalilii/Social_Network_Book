from django.db import models
from user.models import User


# from django.utils import  timezone

# Create your models here.
class Author(models.Model):
    name = models.CharField('name', max_length=30)


class Book(models.Model):
    class Meta:
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب ها'

    STATUS = [('F', 'free'), ('B', 'borrowed'), ('D', 'deprecated')]
    name = models.CharField('name', max_length=100, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='au')
    publish_year = models.DateTimeField('Year of publishing', auto_now=True, null=True)
    image = models.ImageField('books/', blank=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='use')
    liked = models.ManyToManyField('user.User', blank=True)
    record_date = models.DateTimeField('Time to record books', auto_now_add=True)
    update_time = models.DateTimeField('update time', auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS, default='F')

    def change_status(self):
        if self.status == 'F':
            self.status = 'B'
        else:
            self.status = 'F'
        self.save()
        return self.status

    def get_publish_year(self):
        return self.publish_year.year


class Comment(models.Model):
    class Meta:
        ordering = ('-created',)

    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='us')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='bo')
    text = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Like(models.Model):
    LIKE_CHOICE = [("L", "Like"), ("D", "Dislike")]
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='u')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='b')
    like = models.CharField(max_length=3, choices=LIKE_CHOICE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def toggle(self):
        if self.like == "L":
            self.like = "D"
        else:
            self.like = "L"
        self.save()
