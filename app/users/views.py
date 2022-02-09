from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages


def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Usuario não existe!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(request.POST)
            return redirect('dashboard:home')
        else:
            messages.error(request, 'Usuário e/ou password incorrectos')
    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'Usuário deslogado!')
    return redirect('users:login')
