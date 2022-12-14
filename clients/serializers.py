from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from clients.models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['name', 'address']
        # fields = ['name', 'address']