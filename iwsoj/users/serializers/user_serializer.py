from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "email", "password")
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True},
            'email': {'required': True},
            'first_name': {'required': True}
        }

    def create(self, validated_data: dict) -> User:
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
        )
        if validated_data.get('last_name'):
            user.last_name=validated_data['last_name']
        user.set_password(validated_data['password'])
        self._save_user(user)
        return user

    # I needed to mock it out, thus I extracted it
    def _save_user(self, user):
        user.save()
