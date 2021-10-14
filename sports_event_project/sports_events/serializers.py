from rest_framework import serializers
from .models import Sports_event

class Sports_eventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sports_event
        fields = ['id', 'user_id', 'sport', 'name', 'date_time', 'location', 'number_of_players', 'skill_level', 'competitiveness_level', 'lat', 'lng']

        def create(self, validated_data):
            return Sports_event.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.date_time = validated_data.get('date_time', instance.date_time)
            instance.location = validated_data.get('location', instance.location)
            instance.number_of_players = validated_data.get('number_of_players', instance.number_of_players)
            instance.skill_level = validated_data.get('skill_level', instance.skill_level)
            instance.competitiveness_level = validated_data.get('competitiveness_level', instance.competitiveness_level)
            instance.save()
            return instance
