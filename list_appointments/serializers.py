from rest_framework import serializers
from .models import CustomSettings

class HelloSerializer(serializers.ModelSerializer):
    hello = serializers.CharField()

class customSettingsSerializer():
    class Meta:
        model = CustomSettings
        fields = '__all__'
    