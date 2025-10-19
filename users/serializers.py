from django.contrib.auth import get_user_model
from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer

User = get_user_model()

class CustomUserDetailsSerializer(serializers.ModelSerializer):
    # Serializer for returning user details
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile_picture_url')
        read_only_fields = ('id', 'profile_picture_url')


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'password2')

    def validate(self, data):
        # Custom validation for password match and unique email
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({"email": "This email is already registered."})
        return data

    def create(self, validated_data):
        # Create user after validation
        validated_data.pop('password2')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            password=validated_data['password']
        )
        return user


class CustomLoginSerializer(LoginSerializer):
    # Custom login serializer to remove username field
    def get_fields(self):
        fields = super().get_fields()
        fields.pop('username', None)
        return fields
