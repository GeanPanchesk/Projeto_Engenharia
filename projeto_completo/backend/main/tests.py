from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Filme, Carrinho, ItemCarrinho

class SistemaLocacaoTest(TestCase):
    
    def setUp(self):

        # Cria um usuário de teste
        self.user = User.objects.create_user(username='tester', password='password123')
        
        # Loga o usuário 
        self.client.login(username='tester', password='password123')
        
        # Cria um filme de teste
        self.filme = Filme.objects.create(
            nome="Filme Teste",
            nota_imdb=8.5,
            genero="acao",
            sinopse="Sinopse de teste",
            link_trailer="http://youtube.com",
            capa="capa_teste.jpg"
        )
        
        # O Carrinho é criado automaticamente pelo signal 'criar_carrinho' 
        

    def test_simular_locacao(self):
        
        # Teste 1: Simula o usuário alugando um filme (adicionando ao carrinho).
        
        
        url = reverse('add_carrinho', args=[self.filme.id])
        
        # Faz a requisição para adicionar
        response = self.client.get(url)
        
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['ok'], True)
        
        
        carrinho_do_usuario = Carrinho.objects.get(usuario=self.user)
        item_existe = ItemCarrinho.objects.filter(carrinho=carrinho_do_usuario, filme=self.filme).exists()
        
        self.assertTrue(item_existe, "O filme deveria estar no carrinho, mas não foi encontrado.")

    def test_simular_cancelamento(self):
        
        # Teste 2: Simula o usuário cancelando a locação (removendo do carrinho).
        
        # Preparação: Adiciona o item ao carrinho manualmente primeiro
        carrinho_do_usuario = Carrinho.objects.get(usuario=self.user)
        item_locado = ItemCarrinho.objects.create(carrinho=carrinho_do_usuario, filme=self.filme)
        
        # Verifica se o item existe antes de tentar apagar
        self.assertEqual(ItemCarrinho.objects.count(), 1)
        
        url = reverse('remover_item', args=[item_locado.id])
        
        response = self.client.get(url)
        
        self.assertRedirects(response, reverse('carrinho'))
        
        item_existe = ItemCarrinho.objects.filter(id=item_locado.id).exists()
        self.assertFalse(item_existe, "O item deveria ter sido removido, mas ainda existe no banco.")