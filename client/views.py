from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from client.models import Client, Oblast, Rayon
from client.serializers import ClientSerializer, OblastSerializer, RayonSerializer
from .serializers import ClientDataSerializer

class ClientApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        client = Client.objects.all()
        serializer = ClientSerializer(client, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientApiDetailView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, id):
        client = get_object_or_404(Client, id=id)
        serializer = ClientSerializer(client)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        client = get_object_or_404(Client, id=id)
        serializer = ClientSerializer(instance=client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            client = Client.objects.get(id=id)
        except:
            return Response(
                data={
                    'success': False,
                    'message': 'User not fount'
                }
            )
        else:
            client.delete()
            return Response(
                data={
                    'success': True,
                    'message': 'Client successfully delete'
                }
            )


class OblastApiView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        oblast = Oblast.objects.all()
        serializer = OblastSerializer(oblast, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OblastSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OblastApiDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, id):
        oblast = get_object_or_404(Oblast, id=id)
        serializer = OblastSerializer(oblast)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        oblast = get_object_or_404(Oblast, id=id)
        serializer = OblastSerializer(instance=oblast, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            oblast = get_object_or_404(Oblast, id=id)

        except:
            return Response(
                data={
                    'success': False,
                    'message': 'User not found'
                }
            )
        else:
            oblast.delete()
            return Response(
                data={
                    'success': True,
                    'message': 'Oblast successfully deleted'
                }
            )


class RayonApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        rayon = Rayon.objects.all().order_by('-created_at')
        serializer = RayonSerializer(rayon, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer = RayonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RayonDetailApiView(APIView):
    def get(self, request, id):
        rayon = get_object_or_404(Rayon, id=id)
        serializer = RayonSerializer(rayon)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        rayon = get_object_or_404(Rayon, id=id)
        serializer = RayonSerializer(instance=rayon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            rayon = get_object_or_404(Rayon, id=id)
        except:
            return Response(
                data={
                    'success': False,
                    'message': 'User not found'
                }
            )
        else:
            rayon.delete()
            return Response(
                data={
                    'success': True,
                    'message': 'User successfully deleted'
                }
            )
        

class ClientDataAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        client = Client.objects.all()
        serializer = ClientDataSerializer(client, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ClientDataDetailAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, client_id):
        clients = Client.objects.filter(client_id=client_id)
        if not clients.exists():
            return Response({'error': 'Client not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ClientSerializer(clients, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
