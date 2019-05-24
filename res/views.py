from rest_framework import viewsets

from .models import (
    Character,
    World
)

from .serializers import (
    CharacterSerializer,
    WorldSerializer
)


class CharacterViewSet(viewsets.ModelViewSet):

    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    search_fields = ('name',)

    def retrieve(self, request, *args, **kwargs):
        return super(CharacterViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(CharacterViewSet, self).list(request, *args, **kwargs)


class WorldViewSet(viewsets.ModelViewSet):

    queryset = World.objects.all()
    serializer_class = WorldSerializer
    search_fields = ('name',)

    def retrieve(self, request, *args, **kwargs):
        return super(WorldViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(WorldViewSet, self).list(request, *args, **kwargs)