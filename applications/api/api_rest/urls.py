from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    # Rota raiz para mostrar todos os usuários (apenas GET)
    path('', views.list_all_users, name='list_all_users'),

    # Rota /users/ para listar todos (GET) e criar um novo (POST)
    path('users', views.user_list_create, name='user_list_create'),
    
    # Rota /users/<id>/ para operações em um usuário específico (GET, PUT, DELETE)
    # <int:pk> captura um número da URL e o passa como argumento 'pk' para a view.
    path('users/<int:pk>/', views.user_detail_update_delete, name='user_detail_update_delete'),
]