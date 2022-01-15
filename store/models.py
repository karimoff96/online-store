from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media', blank=True, null=True)
    cr_on = models.DateTimeField(auto_now_add=True)
    cr_up = models.DateTimeField(auto_now=True, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media', blank=True, null=True)
    cr_on = models.DateTimeField(auto_now_add=True)
    cr_up = models.DateTimeField(auto_now=True, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    datetime = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media', blank=True, null=True)
    price = models.IntegerField(default=0, blank=True, null=True)
    cr_on = models.DateTimeField(auto_now_add=True)
    cr_up = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Users(models.Model):
    username = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    avatar = models.ImageField(upload_to='media', blank=True, null=True)
    phone_number = models.CharField(max_length=128, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=30, blank=True, null=True)
    cr_on = models.DateTimeField(auto_now_add=True)
    cr_up = models.DateTimeField(auto_now=True, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name
