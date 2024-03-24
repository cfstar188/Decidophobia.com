from rest_framework import serializers
from .models import CustomUser

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