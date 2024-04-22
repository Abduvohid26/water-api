from django.shortcuts import render
from rest_framework import permissions, generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer,  LoginSerializer, UserSerializer
from django.contrib.auth import authenticate
from .models import User


class RegisterUserApiView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]


class LoginUserApiView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        # user = authenticate(username=username, password=password)
        user = User.objects.filter(username=username).first()
        if user is not None:
            return Response(
                data={
                    'id': user.id,
                    'access_token': user.token()['access_token'],
                    'refresh_token': user.token()['refresh_token'],
                    'username': user.username,
                    'user_roles': user.user_roles,

                }, status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data={
                    'success': False,
                    'message': 'username or password invalid'
                }, status=status.HTTP_401_UNAUTHORIZED
            )




class UserApiView(APIView):
    def get(self, request):
        user = User.objects.all().order_by('-created_at')
        serializer = UserSerializer(user, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailApiView(APIView):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = UserSerializer(user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        user = get_object_or_404(User, id=id)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            user = get_object_or_404(User, id=id)
        except:
            return Response(
                data={
                    'success': False,
                    'message': 'User not found'
                }
            )
        else:
            user.delete()
            return Response(
                data={
                    'success': False,
                    'message': 'User successfully deleted'
                }
            )
        

# class WorkerApiView(APIView):
#     def get(self, request):
#         worker = Worker.objects.all()
#         serializer = WorkerSerializer(worker, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = WorkerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class WorkerApiViewDetail(APIView):
#     permission_classes = [permissions.AllowAny]

#     def get(self, request, id):
#         worker = get_object_or_404(Worker, id=id)
#         serializer = WorkerSerializer(worker)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, id):
#         worker = get_object_or_404(Worker, id=id)
#         serializer = WorkerSerializer(data=request.data, instance=worker)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         try:
#             worker = get_object_or_404(Worker, id=id)
#         except:
#             return Response(
#                 data={
#                     'success': False,
#                     'message': 'User not found'
#                 }
#             )
#         else:
#             worker.delete()
#             return Response(
#                 {
#                     'success': True,
#                     'message': 'User successfully deleted'
#                 }
#             )