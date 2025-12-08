from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseForbidden, JsonResponse

from .forms import FilmeForm
from .models import Filme, Carrinho, ItemCarrinho, CatalogoPessoal
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


def detalhes(request, filme_id):
    filme = Filme.objects.get(id=filme_id)
    return render(request, 'main/detalhes.html', {"filme": filme})


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

@login_required
def adicionar_ao_carrinho(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)

    # Evitar duplicado
    if not ItemCarrinho.objects.filter(carrinho=carrinho, filme=filme).exists():
        ItemCarrinho.objects.create(carrinho=carrinho, filme=filme)

    # Quantidade atualizada
    total = ItemCarrinho.objects.filter(carrinho=carrinho).count()

    # Retorna OK + total
    return JsonResponse({"ok": True, "total": total})


@login_required
def carrinho(request):
    carrinho, created = Carrinho.objects.get_or_create(usuario=request.user)
    return render(request, 'main/carrinho.html', {"carrinho": carrinho})

@login_required
def remover_item(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id, carrinho__usuario=request.user)
    item.delete()
    return redirect('carrinho')

@login_required
def carrinho_qtd(request):
    carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)
    total = ItemCarrinho.objects.filter(carrinho=carrinho).count()
    return JsonResponse({"ok": True, "total": total})

def perfil(request):
    catalogo, criado = CatalogoPessoal.objects.get_or_create(user=request.user)
    return render(request, "main/perfil.html", {"catalogo": catalogo})

@login_required
def excluir_conta(request):
    if request.method == "POST":
        user = request.user
        logout(request)   # desloga antes de excluir
        user.delete()     # exclui conta
        return redirect("index")  # volta para home após exclusão
    
    return redirect("perfil")

@login_required
def alugar_filmes(request):

    carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)
    catalogo, _ = CatalogoPessoal.objects.get_or_create(user=request.user)

    # adicionar todos os filmes ao catálogo
    for item in carrinho.itens.all():
        catalogo.filmes.add(item.filme)

    # esvaziar carrinho
    carrinho.itens.all().delete()

    messages.success(request, "Filmes adicionados ao seu catálogo!")

    return redirect('perfil')

@login_required
def remover_do_catalogo(request, filme_id):
    request.user.catalogo.filmes.remove(filme_id)
    return redirect('perfil')





