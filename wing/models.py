from django.db import models

# Create your models here.


class Grocery(models.Model):
    name = models.CharField(max_length=20, default=None)
    price = models.FloatField(default=None)
    image = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.name


class Vegetable(models.Model):
    name = models.CharField(max_length=20, default=None)
    price = models.FloatField(default=None)
    image = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(max_length=20, default=None)
    price = models.FloatField(default=None)
    image = models.ImageField(default='default.png', blank=True)
    def __str__(self):
        return self.name


class Extras(models.Model):
    name = models.CharField(max_length=20, default=None)
    price = models.FloatField(default=None)
    image = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.name


class Users(models.Model):
    user_name = models.CharField(max_length=20, default='John')
    user_age = models.IntegerField(default=23)
    user_email = models.EmailField(default='abc@email.com')

    def __str__(self):
        return self.user_name
