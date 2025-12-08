from django.db import models
from django.contrib.auth.models import User
from main.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_movie_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class Filme(models.Model):
    GENEROS = [
        ('populares', 'Populares na Plataforma'),
        ('familia', 'Para Toda a Família'),
        ('terror', 'Aterrorizantes'),
        ('acao', 'Ação e Aventura'),
        ('independente', 'Cinema Independente'),
    ]

    nome = models.CharField(max_length=200)
    nota_imdb = models.DecimalField(max_digits=3, decimal_places=1)
    genero = models.CharField(max_length=20, choices=GENEROS)
    sinopse = models.TextField()
    link_trailer = models.URLField()
    capa = models.ImageField(upload_to='filmes/')
    destaque = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Carrinho(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def total_itens(self):
        return self.itens.count()

    def total_preco(self):
        return sum(item.preco for item in self.itens.all())

    def __str__(self):
        return f"Carrinho de {self.usuario.username}"

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, related_name="itens", on_delete=models.CASCADE)
    filme = models.ForeignKey('Filme', on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=6, decimal_places=2, default=7.90)

    def __str__(self):
        return f"{self.filme.nome} - R$ {self.preco}"

class CatalogoPessoal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="catalogo")
    filmes = models.ManyToManyField(Filme, blank=True)

    def __str__(self):
        return f"Catálogo de {self.user.username}"


