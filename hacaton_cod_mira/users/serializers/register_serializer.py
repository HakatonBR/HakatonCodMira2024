from rest_framework import serializers
from django.contrib.auth import get_user_model

from users.models.role import Role


User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    password_confirm = serializers.CharField(required=True, write_only=True)
    role = serializers.ChoiceField(choices=Role.choices)

    class Meta:
        model = User
        fields = ['email', 'password', 'password_confirm', 'role']

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')

        if not all([email, password, password_confirm]):
            raise serializers.ValidationError("Все поля обязательны")
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Пользователь с такой почтой уже существует.")
        
        if password != password_confirm:
            raise serializers.ValidationError("Пароли должны совпадать.")
        
        return attrs
    
    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        user = User.objects.create_account(
            email=email,
            password=password,
            role=validated_data['role']
        )

        return user
