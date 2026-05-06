from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Shop(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    
    def __str__(self):
        return self.name