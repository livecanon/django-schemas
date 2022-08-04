from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
# see https://docs.djangoproject.com/en/3.2/topics/auth/default/#the-login-required-decorator
from django.contrib.auth.decorators import login_required
# see https://docs.djangoproject.com/en/3.2/topics/auth/default/#the-loginrequired-mixin
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


def loginUser(request):
    # see https://docs.djangoproject.com/en/3.2/topics/auth/default/#how-to-log-a-user-in

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) # creates a session
            return redirect('profiles')
        else:
            messages.error(request, 'Username or password is incorrect')


    return render(request, 'users/login_register.html')


@login_required
def logoutUser(request):
    logout(request)
    messages.error(request, 'User was logged out')
    return redirect('login')


def profiles(request):
    profiles = Profile.objects.all()

    context = {
        'profiles': profiles
    }
    
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    top_skills = profile.skill_set.exclude(description__exact="")
    other_skills = profile.skill_set.filter(description="")
    
    context = {
        'profile': profile,
        'top_skills': top_skills,
        'other_skills': other_skills,
    }

    return render(request, 'users/user-profile.html', context)
