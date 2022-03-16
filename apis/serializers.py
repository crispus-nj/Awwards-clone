from rest_framework import serializers
from projects.models import Project
from accounts.models import UserAccount

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = UserAccount
        fields = ['username', 'email', 'password', 'is_active', 'is_admin']

    def create(self, validated_data):
        return UserAccount.objects.create_user(**validated_data)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['username', 'email', 'bio']
