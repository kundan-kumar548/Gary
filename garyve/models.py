from django.db import models, migrations
from django.conf import settings
from django.utils import timezone
import datetime

# Create your models here.


class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.localtime())
    # created_date = models.DateTimeField(default=datetime.datetime.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Blog(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline


class Company(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name


class Programmer(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(default=23)
    email = models.EmailField(default="abc@email.com")
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Users(models.Model):
    user_name = models.CharField(max_length=20, default='John')
    user_age = models.IntegerField(default=23)
    user_email = models.EmailField(default='abc@email.com')

    def __str__(self):
        return "{} email is {}".format(self.user_name, self.user_email)
