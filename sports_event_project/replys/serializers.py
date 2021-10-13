from rest_framework import serializers
from .models import Reply

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['id', 'user_id', 'comment']

        def create(self, validated_data):
            return Reply.objects.create(**validated_data)