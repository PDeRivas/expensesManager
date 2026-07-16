from django.contrib.auth import get_user_model
from rest_framework import serializers
from .repository import UserRepository

# Always use get_user_model() to reference your custom user model safely
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password'] # Add your custom fields here

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.repository = UserRepository()

    def create(self, validated_data):
        # .create_user() automatically hashes the password
        return self.repository.create(**validated_data)
