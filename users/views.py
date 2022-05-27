from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from users.models import CustomUser
from users.serializers import CustomUserSerializer


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['username']
    search_fields = ['username', 'city']
    ordering_fields = ['username']
