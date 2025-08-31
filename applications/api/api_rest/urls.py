from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('users', views.users, name='get_all_users'),   # GET todos / POST novo
    path('users/<int:id>', views.user_detail, name='user_detail'),  # GET/PUT/DELETE por ID
]