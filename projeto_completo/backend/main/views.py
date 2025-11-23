from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm


def index(request):
    return render(request, 'main/index.html')

def index_login(request):
    return render(request, 'main/index_login.html')

def index_cadastro(request):
    return render(request, 'main/index_cadastro.html')

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




