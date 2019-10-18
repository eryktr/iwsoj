from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "email", "password")
        write_only_fields = ('password',)
        read_only_fields = ('id',)

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
