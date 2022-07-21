from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate


def home(request):
    return render(request, 'myApp/home.html')


def sign_up(request):
    # here when request is 'get' request then render the page
    # if 'post' then create user account
    if request.method == "POST":
        # so if we have POST request then we will fill the register form with what ever the data was in the form
        form = RegisterForm(request.POST)
        # so here we are just trying to render the 'form' inside the 'sign-up' page
        # but we also have to create the user when there is 'POST' request
        if form.is_valid():
            user = form.save()
            # now here we will save the user
            login(request, user)
            # after we create the user now we can login the user
            return redirect('/home')
            # and we will redirect to '/home'
    else:
        form = RegisterForm()
        # if we have GET request then we will create the form with empty which doesn't have any data
    # and we will render that as 'form' UI inside the 'sign_up.html' page
    # NOTE: 'form' is the default form provided by django which we customize inside the 'forms.py'
    # where we have access the 'form' data and rendering that form UI there
    return render(request, 'registration/sign_up.html', {"form": form})
