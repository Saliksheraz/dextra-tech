from django.contrib.auth.forms import UserCreationForm
from django import forms


#################### Django User Registration Form to Register a new User ###########
class UserRegisterForm(UserCreationForm):
    firstName = forms.CharField(max_length=100)
    secondName = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100, required=False)
    address = forms.CharField(max_length=300)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
        ('ratherNotSay', 'Rather Not Say')
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    picture = forms.ImageField(required=False)
    mobile = forms.CharField(max_length=100)
    website = forms.CharField(max_length=100, required=False)
    facebook = forms.CharField(max_length=100, required=False)
    insta = forms.CharField(max_length=100, required=False)
    email = forms.EmailField()
