from rest_framework import serializers
from .models import Attending_athlete

class Attending_athleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attending_athlete
        fields = ['id', 'user_id', 'sports_event']

        def create(self, validated_data):
            return Attending_athlete.objects.create(**validated_data)