from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateform, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile

def register(request):
    #use django's  own form
    #to get data from user and submit it in database
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #to save the new user is as simple as calling the save function
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
        """ profile = UserProfile() """ 
    else:
        form = UserRegisterForm()
    return render(request, "/home/marwa254/Desktop/DELIGHT/mysite/Users/templates/Users/register.html", {'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        U_form = UserUpdateform(request.POST)
        if U_form.is_valid():
            #this form is for updating the user's email and maybe name
            U_form.save()
            messages.success(request, 'Details updated succesfully!!')
            return redirect('home')
        """ profile = UserProfile() """ 
    else:
        Context = {
            "Details" : Profile.objects.all
        }
        return render(request, "/home/marwa254/Desktop/DELIGHT/mysite/Users/templates/Users/profile.html", Context )

