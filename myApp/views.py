from django.shortcuts import render
from .forms import RegisterForm


def home(request):
    return render(request, 'myApp/home.html')


def sign_up(request):
    # here when request is 'get' request then render the page
    # if 'post' then create user account
    if request.method == "POST":
        # so if we have POST request then we will fill the register form with what ever the data was in the form
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()
        # if we have GET request then we will create the form with empty which doesn't have any data
    # and we will render that as 'form' UI inside the 'sign_up.html' page
    # NOTE: 'form' is the default form provided by django which we customize inside the 'forms.py'
    # where we have access the 'form' data and rendering that form UI there
    return render(request, 'registration/sign_up.html', {"form": form})
