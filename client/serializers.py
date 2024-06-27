from rest_framework import serializers

from client.models import Client, Oblast, Rayon


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'client_id', 'username', 'phone_number', 'latitude',
                  'longitude', 'region', 'description', 'image', 'created_at']


class OblastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oblast
        fields = ['id', 'created_at', 'name']


class RayonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rayon
        fields = ['id', 'created_at', 'name', 'oblast']


class ClientDataSerializer(serializers.ModelSerializer):
    region = RayonSerializer()

    class Meta:
        model = Client
        fields = ['id', 'client_id', 'username', 'phone_number', 'latitude',
                  'longitude', 'region', 'description', 'image', 'created_at']
