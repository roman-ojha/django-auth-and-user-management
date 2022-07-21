# here we will create the registration form
from django import forms

# we will extend the user creation form which is the default form from django
from django.contrib.auth.forms import UserCreationForm
#  import user where we will going to store different user
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    # here we are adding form to a default UserCreationForm called 'email'
    email = forms.EmailField(required=True)
    # so here we are adding 'email' as custom form which doesn't include inside the default django UserCreationForm

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # and inside the form we want to include 'username', 'email', 'password1', 'password2'
