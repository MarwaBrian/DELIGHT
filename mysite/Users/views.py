from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

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
    else:
        form = UserRegisterForm()
    return render(request, "/home/marwa254/Desktop/DELIGHT/mysite/Users/templates/Users/register.html", {'form':form})


@login_required
def profile(request):
    return render(request, "/home/marwa254/Desktop/DELIGHT/mysite/Users/templates/Users/profile.html" )
