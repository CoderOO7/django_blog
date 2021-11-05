from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm
from django.contrib import messages
from .decorators import unauthenticated_user

@unauthenticated_user
def auth_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            full_name = f'{first_name} {last_name}'
            messages.success(request, f'Account created for {full_name}!')
            return redirect('users-login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@unauthenticated_user
def auth_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password1')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog-home')
        else:
            messages.error(request, 'Incorrect email or password')

    return render(request, 'users/login.html')


def auth_logout(request):
    logout(request)
    return redirect('users-login')
