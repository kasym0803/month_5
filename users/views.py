import random
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.views import APIView

from users.models import Confirm
from users.serializer import RegisterSerializer, ConfirmPasswordSerializer, LoginSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(**serializer.validated_data, is_active=False)
        confirmation = Confirm.objects.create(user=user, code=random.randint(100000, 999999))
        return Response({'code': confirmation.code}, status=201)


# @api_view(['POST'])
# def register(request):
#     serializer = RegisterSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = User.objects.create_user(**serializer.validated_data, is_active=False)
#     confirmation = Confirm.objects.create(user=user, code=random.randint(100000, 999999))
#     return Response({'code': confirmation.code}, status=201)


class ConfirmView(APIView):
    def post(self, request):
        serializer = ConfirmPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data.get('code', None)
        confirmation = get_object_or_404(Confirm, code=code)
        user = confirmation.user
        user.is_active = True
        user.save()
        return Response({'status': 'success'}, status=200)


# @api_view(['POST'])
# def confirm(request):
#     serializer = ConfirmPasswordSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     code = serializer.validated_data.get('code', None)
#     confirmation = get_object_or_404(Confirm, code=code)
#     user = confirmation.user
#     user.is_active = True
#     user.save()
#     return Response({'status': 'success'}, status=200)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, **serializer.validated_data)
        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            user.save()
            return Response({'token': token.key})

        return Response({'error': 'Invalid data'}, status=400)


# @api_view(['POST'])
# def login_view(request):
#     serializer = LoginSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = authenticate(request, **serializer.validated_data)
#     if user:
#         login(request, user)
#         token, created = Token.objects.get_or_create(user=user)
#         user.save()
#         return Response({'token': token.key})
#
#     return Response({'error': 'Invalid data'}, status=400)
