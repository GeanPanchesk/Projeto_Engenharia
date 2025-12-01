from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import Filme

from django.http import HttpResponseForbidden

from .forms import FilmeForm
from .models import Filme
from django.contrib.auth.decorators import login_required

def index(request):
    destaque = Filme.objects.filter(destaque=True).first()
    populares = Filme.objects.filter(genero='populares')
    familia = Filme.objects.filter(genero='familia')
    terror = Filme.objects.filter(genero='terror')
    acao = Filme.objects.filter(genero='acao')
    independente = Filme.objects.filter(genero='independente')

    categorias = [
        ('Populares na Plataforma', populares),
        ('Para Toda a Família', familia),
        ('Aterrorizantes', terror),
        ('Ação e Aventura', acao),
        ('Cinema Independente', independente),
    ]

    return render(request, 'main/index.html', {
        'destaque': destaque,
        'categorias': categorias,
    })


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

@login_required
def add_filme(request):
    mensagens = ""
    if request.method == "POST":
        nome = request.POST.get("nome")
        nota_imdb = request.POST.get("nota_imdb")
        genero = request.POST.get("genero")
        sinopse = request.POST.get("sinopse")
        link_trailer = request.POST.get("link_trailer")
        capa = request.FILES.get("capa")
        destaque = request.POST.get("destaque") == "on"

        # Salvar no banco
        filme = Filme.objects.create(
            nome=nome,
            nota_imdb=nota_imdb,
            genero=genero,
            sinopse=sinopse,
            link_trailer=link_trailer,
            capa=capa,
            destaque=destaque
        )
        mensagens = f"Filme '{filme.nome}' adicionado com sucesso!"

    filmes = Filme.objects.all().order_by('-id')  # lista de filmes cadastrados

    return render(request, "main/add_filme.html", {
        "filmes": filmes,
        "mensagens": mensagens
    })

@login_required
def remover_filme(request, filme_id):
    if request.method == "POST":
        filme = get_object_or_404(Filme, id=filme_id)
        filme.delete()
    return redirect('add_filme')




