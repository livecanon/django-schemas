from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CustomUserCreationForm



def login_view(request):
    if request.user.is_authenticated:
        return redirect('/blog/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/blog/')
        else:
            context = {
                'error': 'Invalid credentials'
            }
            return render(request, 'accounts/login.html', context=context)
    return render(request, 'accounts/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('/auth/login/')


class SignUpView(SuccessMessageMixin, CreateView):
    # see https://docs.djangoproject.com/en/4.0/ref/contrib/messages/#displaying-messages
    # see https://stackoverflow.com/questions/62935406
    # see https://docs.djangoproject.com/en/4.0/topics/auth/default/#django.contrib.auth.forms.UserCreationForm
    model = User
    template_name = 'accounts/register.html'
    form_class = CustomUserCreationForm
    success_url = '/auth/login'
    success_message = "User was created successfully. You can sign in now :)"
