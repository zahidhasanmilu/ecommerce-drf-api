from rest_framework import generics

from accounts.models import User
from .serializers import RegisterSerializer

class RegisterView(generics.ListCreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    
    
