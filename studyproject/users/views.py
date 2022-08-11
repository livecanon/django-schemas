from django.shortcuts import render, redirect
from .models import Profile, Message
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
# see https://docs.djangoproject.com/en/3.2/topics/auth/default/#the-login-required-decorator
from django.contrib.auth.decorators import login_required
# see https://docs.djangoproject.com/en/3.2/topics/auth/default/#the-loginrequired-mixin
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm, SkillForm, MessageForm
from .utils import searchProfiles, paginateProfiles


def loginUser(request):
    # see https://docs.djangoproject.com/en/3.2/topics/auth/default/#how-to-log-a-user-in

    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) # creates a session
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')

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
            return redirect('edit-account')
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

    profiles, search_query = searchProfiles(request)
    custom_range, profiles = paginateProfiles(request, profiles, 3)

    context = {
        'profiles': profiles,
        'search_query': search_query, # keep search value in input
        'custom_range': custom_range,
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


@login_required(login_url='login')
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


@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    message_requests = profile.messages.all()
    unread_count = message_requests.filter(is_read=False).count()

    context = {
        'message_requests': message_requests,
        'unread_count': unread_count,
    }

    return render(request, 'users/inbox.html', context=context)


@login_required(login_url='login')
def viewMessage(request, pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if not message.is_read:
        message.is_read = True
        message.save()

    context = {
        'message': message
    }
    return render(request, 'users/message.html', context)


def createMessage(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()
    try:
        sender = request.POST.get('sender')
    except:
        sender = None

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender # Either person who send it or None
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email
        
            message.save()
            messages.success(request, 'Your message was successfully sent!')
            return redirect('user-profile', pk=recipient.id)
            
    context = {
        'recipient': recipient,
        'form': form
    }
    return render(request, 'users/message_form.html', context)
