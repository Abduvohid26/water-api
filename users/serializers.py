from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)
    confirm_password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'phone_number1',
            'user_roles',
            'password',
            'confirm_password'
        )

    def create(self, validated_data):
        user = super(RegisterSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        print(user)
        user.save()
        return user

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        confirm_password = data.pop('confirm_password', None)

        if username and User.objects.filter(username=username).exists():
            raise ValidationError({'username': 'Username already exists'})

        if password != confirm_password:
            raise ValidationError({'confirm_password': 'Passwords do not match'})
        print(data)
        return data


# class WorkerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Worker
#         fields = [
#             'id',
#             'username',
#             'phone_number',
#             'worker_roles',
#             'description',
#             'created_at',
#         ]


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'user_roles', 'created_at', 'phone_number1',
                  'phone_number2', 'latitude', 'longitude', 'latitude1', 'longitude1', 'balance']

