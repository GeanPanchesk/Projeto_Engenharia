from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),  # rota raiz
    path('login/', views.index_login, name='index_login'),
    path('cadastro/', views.register, name='index_cadastro'),
    path('detalhes/<int:filme_id>/', views.detalhes, name='detalhes'),
    path('add-filme/', views.add_filme, name='add_filme'),
    path('logout/', LogoutView.as_view(next_page='index_login'), name='logout'),
    path('remover-filme/<int:filme_id>/', views.remover_filme, name='remover_filme'),
    path("carrinho/", views.carrinho, name="carrinho"),
    path("carrinho/add/<int:filme_id>/", views.adicionar_ao_carrinho, name="add_carrinho"),
    path("carrinho/remover/<int:item_id>/", views.remover_item, name="remover_item"),
    path("carrinho/qtd/", views.carrinho_qtd, name="carrinho_qtd"),
    path("perfil/", views.perfil, name="perfil"),
    path("excluir_conta/", views.excluir_conta, name="excluir_conta"),
    
]
