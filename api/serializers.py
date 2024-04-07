from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from api.models import CustomUser, Message, Chat, ChatMember, StatusUser


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token


class CustomUserSerializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = ''


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'password2', 'email', 'bio', 'photo')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Пароли не совпадают'})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            bio=validated_data['bio'],
            photo=validated_data['photo'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class MessageSerializer(serializers.ModelSerializer):
    class Meta():
        model = Message
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):
    class Meta():
        model = Chat
        fields = '__all__'


class ChatMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMember
        fields = '__all__'


class StatusUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusUser
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
