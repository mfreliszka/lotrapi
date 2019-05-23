from rest_framework import serializers

from .models import (
    Character,
    World
)


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('name', 'gender')


class WorldSerializer(serializers.ModelSerializer):
    class Meta:
        model = World
        fields = ('name',)