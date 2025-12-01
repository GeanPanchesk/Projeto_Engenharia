from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomUserCreationForm

from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden


def index(request):
    return render(request, 'main/index.html')

def index_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')  # ou outra página depois do login
        else:
            messages.error(request, "Usuário ou senha incorretos!")

    return render(request, 'main/index_login.html')

def trailer(request):
    return render(request, 'main/trailer.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/index_cadastro.html', {'form': form})

def add_filme(request):
    if not request.user.is_authenticated or not request.user.profile.is_movie_admin:
        return HttpResponseForbidden("Você não tem permissão para acessar esta página.")

    return render(request, "main/add_filme.html")




