from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'myApp/home.html')


def sign_up(request):
    # here when request is 'get' request then render the page
    # if 'post' then create user account
    if request.method == "POST":
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {"form": form})
