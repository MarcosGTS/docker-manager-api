from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

@api_view(['GET'])
def list_all_users(request):
    """
    View para listar todos os usuários. Atenderá a rota raiz ('/').
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({
            "message": f"{len(users)} usuários encontrados",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def user_list_create(request):
    """
    View para listar todos os usuários ou criar um novo usuário.
    Atenderá a rota '/users/'.
    """
    # --- GET (Listar todos) ---
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({
            "message": f"{len(users)} usuários encontrados",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # --- POST (Criar novo) ---
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Usuário cadastrado com sucesso!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": "Erro ao cadastrar usuário. Verifique os dados.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_update_delete(request, pk: int):
    """
    View para buscar, atualizar ou deletar um usuário específico pelo seu ID (pk).
    Atenderá a rota '/users/<id>/'.
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({
            "message": f"Usuário com ID '{pk}' não encontrado."
        }, status=status.HTTP_404_NOT_FOUND)

    # --- GET (Buscar um) ---
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response({
            "message": "Usuário encontrado",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # --- PUT (Atualizar um) ---
    elif request.method == 'PUT':
        # partial=True permite atualizações parciais (PATCH)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Usuário atualizado com sucesso!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            "message": "Erro ao atualizar usuário. Verifique os dados.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    # --- DELETE (Deletar um) ---
    elif request.method == 'DELETE':
        user.delete()
        # É comum retornar 204 (No Content) após um delete bem sucedido
        return Response(status=status.HTTP_204_NO_CONTENT)