from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Carrinho

@receiver(post_save, sender=User)
def criar_carrinho(sender, instance, created, **kwargs):
    if created:
        Carrinho.objects.create(usuario=instance)
