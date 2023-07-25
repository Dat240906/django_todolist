from rest_framework import serializers
from .models import User, Service


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class ServiceSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('title', 'time')