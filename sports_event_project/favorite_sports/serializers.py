from rest_framework import serializers
from .models import Favorite_sport

class Favorite_sportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite_sport
        fields = ['id', 'user_id', 'sport_id']

        def create(self, validated_data):
            return Favorite_sport.objects.create(**validated_data)