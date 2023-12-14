# ecommerce_app/serializers.py

from rest_framework import serializers
from .models import Order
from django.contrib.auth.models import User

class UserSerializerInsert(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
class UserSerializerVal(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
class OrderSerializerStatus(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']