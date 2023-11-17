from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
from .models import Profile
from django.contrib.auth.models import User

def signup_view(request):
    if request.method == 'POST':
        if 'signup_form' in request.POST:
            register_form = SignUpForm(request.POST)
            if register_form.is_valid():
                name = register_form.cleaned_data.get('username')
                job_title = register_form.cleaned_data.get('job_title')
                if any(char.isdigit() for char in name) or any(char.isdigit() for char in job_title):
                    register_form.add_error('username', 'Name and job title should not contain numbers')
                if len(name) < 4:
                    register_form.add_error('username', 'Name should be at least 4 characters long')
                if len(job_title) < 14:
                    register_form.add_error('job_title', 'Job title should be at least 14 characters long')
                if not register_form.errors:
                    user = register_form.save()
                    Profile.objects.create(user=user, job_title=job_title)
                    return redirect('members')


        elif 'login_form' in request.POST:
            print("Sign-in")

        else:
            register_form = SignUpForm()
            login_form = SignInForm(request)
    # return render(request, 'signup.html', {'form': form})
    else:
        register_form = SignUpForm()
        login_form = SignInForm(request)
    return render(request, 'signup.html', {'register_form': register_form, 'login_form': login_form})



def members_view(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        return render(request, 'members.html', {'users': users})
    else:
        return redirect('signup')

def profile_view(request, user_id):
    if request.user.is_authenticated:
        user = User.objects.get(id=user_id)
        profile = Profile.objects.get(id=user_id-2)
        return render(request, 'profile.html', {'username': user.username, 'job_title': profile.job_title})
    else:
        return redirect('signup')