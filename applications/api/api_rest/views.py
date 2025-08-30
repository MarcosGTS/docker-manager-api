from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

# GET all + POST, com suporte a query param ?id=
@api_view(['GET', 'POST'])
def users(request):
    # --- GET ---
    if request.method == 'GET':
        user_id = request.GET.get('id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                serializer = UserSerializer(user)
                return Response({
                    "message": "Usuário encontrado",
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({
                    "message": f"Usuário '{user_id}' não encontrado"
                }, status=status.HTTP_404_NOT_FOUND)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response({
                "message": f"{len(users)} usuários encontrados",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

    # --- POST ---
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Usuário cadastrado com sucesso!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": "Erro ao cadastrar usuário. Verifique os dados e tente novamente.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


# GET by ID + PUT + DELETE (URL param)
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response({
            "message": f"Usuário '{id}' não encontrado."
        }, status=status.HTTP_404_NOT_FOUND)

    # --- GET ---
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response({
            "message": "Usuário encontrado",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    # --- PUT ---
    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Usuário atualizado com sucesso!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            "message": "Erro ao atualizar usuário. Verifique os dados e tente novamente.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    # --- DELETE ---
    if request.method == 'DELETE':
        user.delete()
        return Response({
            "message": f"Usuário '{id}' excluído com sucesso!"
        }, status=status.HTTP_204_NO_CONTENT)
