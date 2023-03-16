from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#we can't use usermodel but we need to import Profile model to be able to work with the profile photo
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=200)
    middle_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'username', 'email', 'password1', 'password2']


#creating a form that interacts with our database using Modelform
class UserUpdateform(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', ]

#for updating the user's DP
class ProfileUpdateForm():
    class Meta:
        model = Profile
        fields = ['image']


#next task is to add to views then add it to the profile.html for the procedure to be complete


