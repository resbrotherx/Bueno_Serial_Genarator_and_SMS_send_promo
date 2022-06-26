from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class SoledSerializer(serializers.ModelSerializer):
	class Meta:
		model = SoledSerial
		fields = '__all__'


class ArchivedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archive
        fields = '__all__'