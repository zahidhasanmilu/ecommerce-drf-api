from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm', 'role')

    # Single field validation (Username)
    def validate_username(self, value):
        if value.isdigit(): 
            raise serializers.ValidationError("Username can't be just a number.")
        return value

    # Object-level validation (Multiple fields check)
    def validate(self, data):
        # Password match check
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({"password_confirm": "Password fields didn't match."})
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')        
        user = User.objects.create_user(**validated_data)
        return user