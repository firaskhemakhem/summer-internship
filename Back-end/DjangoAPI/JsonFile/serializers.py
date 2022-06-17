from rest_framework import serializers 
from JsonFile.models import User,JsonfileModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['Login','Email']

class JsonfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = JsonfileModel
        fields = ['Name','Details']