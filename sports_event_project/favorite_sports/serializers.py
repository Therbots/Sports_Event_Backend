from rest_framework import serializers
from .models import Favorite_sport
from sports.serializers import SportSerializer

class Favorite_sportSerializer(serializers.ModelSerializer):
    sport = SportSerializer()
    class Meta:
        model = Favorite_sport
        fields = ['id', 'user_id', 'sport']

        def create(self, validated_data):
            return Favorite_sport.objects.create(**validated_data)