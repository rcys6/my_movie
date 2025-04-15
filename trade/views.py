from django.shortcuts import render
from rest_framework import viewsets

from .models import Card
from .serializer import CardSerialzer
from .permision import IsAdminUserOrReadOnly


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerialzer
    permission_classes = [IsAdminUserOrReadOnly] # 权限类
