from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
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
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
