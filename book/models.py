from django.db import models
#from django.utils import  timezone

# Create your models here.
class Author(models.Model):
    name = models.CharField('name', max_length=30)


class Book(models.Model):
    class Meta:
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب ها'
    STATUS = [('F', 'free'), ('B', 'borrwed'), ('D', 'deprecated')]
    name = models.CharField('name', max_length=100, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True)
    publich_year = models.DateTimeField('Year of publichation')
    record_date = models.DateTimeField('Time to record books', auto_now_add=True)
    update_time = models.DateTimeField('update time', auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS)

    @property
    def full_name(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name}'

    def change_status(self):
        if self.status == 'F':
            self.status = 'B'
        else:
            self.status = 'F'
        self.save()
        return self.status

    def get_publish_yeat(self):
        return self.publich_year.year