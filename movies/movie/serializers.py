from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movies

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='users-detail')

    class Meta:
        model = User
        fields = ('url', 'id', 'first_name', 'last_name', 'phone_no', 'email', 'password', 'is_active', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        is_active = validated_data.pop('is_active')
        is_superuser = validated_data.pop('is_superuser')
        instance.set_password(password)
        instance.is_active = is_active
        instance.is_superuser = is_superuser
        instance.save()
        return instance


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movies
        fields = ['url', 'movie_name', 'short_desc', 'long_desc', 'thumbnail_url', 'movie_url', 'genre']


class CurrUserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='currentuser-detail')

    class Meta:
        model = User
        fields = ('url', 'id', 'first_name', 'last_name', 'phone_no', 'email', 'password')
        extra_kwargs = {'id': {'read_only': True}, 'first_name': {'read_only': True},
                        'last_name': {'read_only': True}, 'phone_no': {'read_only': True},
                        'email': {'read_only': True}, 'password': {'write_only': True}}

    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        instance.set_password(password)
        instance.save()
        return instance



