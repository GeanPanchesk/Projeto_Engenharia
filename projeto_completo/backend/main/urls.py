from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # rota raiz
    path('login/', views.index_login, name='index_login'),
    path('cadastro/', views.register, name='index_cadastro'),
    path('trailer/', views.trailer, name='trailer'),
    
]
