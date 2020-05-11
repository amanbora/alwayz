from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

from alwayz.models import Song

# Create your views here.
def index(request, path=''):
    return render(request, 'index.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_class = (ReadOnly, )

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = serializers.SongSerializer
    permission_class = (permisssions.IsAuthenticatedOrReadOnly, )

    def
