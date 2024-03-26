from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['username'] = self.user.username
        data['avatar'] = 'http://localhost:8000' + self.user.profile_picture.url if self.user.profile_picture else None
        return data


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=False, default='')
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    full_name = serializers.CharField(required=False)
    profile_picture = serializers.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'password2',
                  'email', 'full_name',
                  'profile_picture')
        extra_kwargs = {
            'full_name': {'required': False}
        }

    def validate(self, attrs):
        if attrs['username'] and CustomUser.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError("Username already exists.")
        if attrs['email'] and CustomUser.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError("Email address already exists.")
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data.get('username', ''),
            email=validated_data.get('email', ''),
            full_name=validated_data.get('full_name', ''),
            profile_picture=validated_data.get('profile_picture', ''),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"Password fields do not match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"Old password is incorrect"})

        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()

        return instance
