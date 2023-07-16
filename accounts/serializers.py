from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        
class CustomAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ['password']
