from rest_framework import serializers
from .models import Leave,GetLeave
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','id']

class LeaveSerializer(serializers.ModelSerializer):
    class Meta :
        model = Leave
        fields = '__all__'

class GetLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetLeave
        fields = ['user','leave','days']