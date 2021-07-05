from django.db import models


# Create your models here.
class User(models.Model):
    GENDER_CHOICES = [('F', 'female'), ('M', 'male')]
    first_name = models.CharField('first name', max_length=100, null=True)
    last_name = models.CharField('last name', max_length=100, null=True, blank=True)
    username = models.CharField('username', max_length=50, unique=True)
    # profile = models.TextField('description', max_length=150)
    gender = models.CharField('gender', max_length=1, choices=GENDER_CHOICES, default='F')
    phone_number = models.CharField('phone number', max_length=11, blank=True)
    biography = models.CharField('biography', max_length=100, null=True)
    country = models.CharField('country', max_length=20, null=True)
    website = models.URLField('website')
    email = models.EmailField('email')
    register_date = models.DateTimeField('register date', auto_now_add=True)
    update_date = models.DateTimeField('update date')
    credit = models.IntegerField('credit', default=20, )
    friends = models.ManyToManyField('user.User', blank=True)

    @property
    def full_name(self):
        return f'{self.first_name},{self.last_name}'

    def __str__(self):
        return f'{self.username} registered at {self.register_date}'

    def delete(self, **kwargs):
        deleted_obj = f'{self.first_name} {self.last_name} object deleted!'
        self.delete()
        return deleted_obj

    def update_credit(self, amount):
        self.credit += amount
        self.save()


class Relationship(models.Model):
    STATUS_CHOICES = [('A', 'accepted'), ('R', 'requested'), ('N', 'name')]
    sender = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name="se")
    receiver = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name="re")
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='N')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} {self.receiver} {self.status} '
