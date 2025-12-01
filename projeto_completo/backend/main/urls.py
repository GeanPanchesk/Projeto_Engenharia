from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),  # rota raiz
    path('login/', views.index_login, name='index_login'),
    path('cadastro/', views.register, name='index_cadastro'),
    path('trailer/', views.trailer, name='trailer'),
    path('add-filme/', views.add_filme, name='add_filme'),
    path('logout/', LogoutView.as_view(next_page='index_login'), name='logout'),

    
]
