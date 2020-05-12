from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .models import Song
from . import serializers


# Create your views here.
def index(request, path=''):
    return render(request, 'index.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly, )

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = serializers.SongSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly, )

    def save_like(self,serializer):
        serializer.save(user=self.request.user)
