from django.db import models
from django.contrib.auth.models import User

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


