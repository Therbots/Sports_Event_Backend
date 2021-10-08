from rest_framework import serializers
from .models import Event_message_board

class Event_message_boardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event_message_board
        fields = ['id', 'sports_event_id']

        def create(self, validated_data):
            return Event_message_board.objects.create(**validated_data)