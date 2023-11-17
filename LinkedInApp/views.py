from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
from .models import Profile
from django.contrib.auth.models import User

def signup_view(request):
    if request.method == 'POST':
        print(request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('username')
            job_title = form.cleaned_data.get('job_title')
            if any(char.isdigit() for char in name) or any(char.isdigit() for char in job_title):
                form.add_error('username', 'Name and job title should not contain numbers')
            if len(name) < 4:
                form.add_error('username', 'Name should be at least 4 characters long')
            if len(job_title) < 14:
                form.add_error('job_title', 'Job title should be at least 14 characters long')
            if not form.errors:
                user = form.save()
                Profile.objects.create(user=user, job_title=job_title)
                return redirect('members')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})




# def signup_view(request):
#     if request.method == 'POST':

#         print(request.POST)
#         #if request.POST.get("id") == "signup_form":

#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data.get('username')
#             job_title = form.cleaned_data.get('job_title')
#             # email = form.cleaned_data.get('email')
#             if any(char.isdigit() for char in name) or any(char.isdigit() for char in job_title):
#                 form.add_error('username', 'Name and job title should not contain numbers')
#             if len(name) < 4:
#                 form.add_error('username', 'Name should be at least 4 characters long')
#             if len(job_title) < 14:
#                 form.add_error('job_title', 'Job title should be at least 14 characters long')
#             if not form.errors:
#                 user = form.save()
#                 Profile.objects.create(user=user, job_title=job_title)
#                 return redirect('members')
#     else:
#         form = SignUpForm(request.POST)
# # login logic

#     # return render(request, 'signup.html', {'form1': form1, 'form2': form2})
#     return render(request, 'signup.html', {'form': form})





def members_view(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        return render(request, 'members.html', {'users': users})
    else:
        return redirect('signup')

def profile_view(request, user_id):
    if request.user.is_authenticated:
        user = User.objects.get(id=user_id)
        profile = Profile.objects.get(id=user_id)
        return render(request, 'profile.html', {'username': user.username, 'job_title': profile.job_title})
    else:
        return redirect('signup')