from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ShopSerializer
from . models import Shop

from rest_framework.permissions import IsAuthenticated
from core.permissions import IsOwnerOrReadOnly,IsShopOwnerOrReadOnly
# Create your views here.

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly, IsShopOwnerOrReadOnly]
    
    
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
    