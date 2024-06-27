from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'phone_number1',
            'user_roles',
            'password',
        )

    def create(self, validated_data):
        user = super(RegisterSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        print(user)
        user.save()
        return user

    def validate(self, data):
        username = data.get('username')

        if username and User.objects.filter(username=username).exists():
            raise ValidationError({'username': 'Username already exists'})
        return data


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'user_roles', 'created_at', 'phone_number1',
                  'phone_number2', 'latitude', 'longitude', 'latitude1', 'longitude1', 'balance']

