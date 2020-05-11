from django.contrib.auth.models import User
from rest_framework import serializers
from alwayz.models import Song

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'firstname', 'lastname')

class SongSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Song
        fields = ('id', 'name', 'date', 'like')

