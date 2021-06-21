from django.db import models


# Create your models here.
class Book(models.Model):
    book_name = models.CharField('book name', max_length=100, null=True, blank=True)
    author_book = models.CharField('Author book', max_length=100, null=True, blank=True)
    public_year = models.CharField('Year of publication', max_length=50)
    time_record_book = models.DateTimeField('Time to record books')
    user_name = models.CharField('user name', max_length=100)
    update_time = models.DateTimeField('update time')

    @property
    def full_name(self):
        return f'{self.book_name},{self.author_book}'

    def __str__(self):
        return f'{self.book_name} and {self.update_time}'
