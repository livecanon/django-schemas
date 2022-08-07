from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
# see https://docs.djangoproject.com/en/3.2/topics/auth/default/#the-login-required-decorator
from django.contrib.auth.decorators import login_required
# see https://docs.djangoproject.com/en/3.2/topics/auth/default/#the-loginrequired-mixin
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm, SkillForm


def loginUser(request):
    # see https://docs.djangoproject.com/en/3.2/topics/auth/default/#how-to-log-a-user-in

    page = 'login'
    
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
            return redirect('user-account')
        else:
            messages.error(request, 'Username or password is incorrect')


    return render(request, 'users/login_register.html')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account was created')
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'An error has occured during registration')


    context = {
        'page': page,
        'form': form
    }
    
    return render(request, 'users/login_register.html', context)


@login_required
def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out')
    return redirect('login')


def profiles(request):
    profiles = Profile.objects.all()

    context = {
        'profiles': profiles
    }
    
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    # see https://docs.djangoproject.com/en/3.2/topics/db/queries/#related-objects
    top_skills = profile.skill_set.exclude(description__exact="")
    other_skills = profile.skill_set.filter(description="")
    
    context = {
        'profile': profile,
        'top_skills': top_skills,
        'other_skills': other_skills,
    }

    return render(request, 'users/user-profile.html', context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    # print(dir(request.user))
    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects
    }
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {
        'form': form
    }
    return render(request, 'users/profile_form.html', context)


@login_required
def createSkill(request):
    form = SkillForm()
    profile = request.user.profile

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Skill was added successfully!')
            return redirect('account')

    context = {
        'form': form
    }
    return render(request, 'users/skill_form.html', context)


@login_required
def updateSkill(request, pk):
    # see https://docs.djangoproject.com/en/4.0/topics/db/examples/one_to_one/
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk) # Ensure only the owner can get it
    # see https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill was updated successfully!')
            return redirect('account')

    context = {
        'form': form
    }
    return render(request, 'users/skill_form.html', context)


def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)

    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill was deleted successfully!')
        return redirect('account')

    context = {
        'object': skill
    }
    return render(request, 'delete.html', context)
