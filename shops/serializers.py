from rest_framework import serializers
from .models import Shop

class ShopSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Shop
        fields = '__all__'