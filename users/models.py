from django.db import models
from django.contrib.auth.models import User, Group


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    picture = models.ImageField(null=True, blank=True)
    firstName = models.CharField(max_length=30, null=True, blank=True)
    secondName = models.CharField(max_length=30, null=True, blank=True)
    website = models.CharField(max_length=30, null=True, blank=True)
    facebook = models.CharField(max_length=30, null=True, blank=True)
    insta = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True)
    numLevel = models.IntegerField(null=True)

    def __str__(self):
        return str(self.user)
