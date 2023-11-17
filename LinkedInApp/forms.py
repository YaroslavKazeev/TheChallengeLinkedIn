from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    job_title = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'job_title',]

class SignInForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password',]