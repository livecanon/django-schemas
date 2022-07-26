from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/blog/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/blog/')
        else:
            context = {
                'errors': 'Invalid username or password'
            }
            return render(request, 'accounts/login.html', context=context)
    return render(request, 'accounts/login.html')

@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/auth/login/')
    return render(request, 'accounts/logout.html')