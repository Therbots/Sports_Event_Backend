from rest_framework import serializers
from .models import Competitiveness_level

class Competitiveness_levelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competitiveness_level
        fields = ['id', 'user_id', 'sport', 'level']

        def create(self, validated_data):
            return Competitiveness_level.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.level = validated_data.get('level', instance.level)
            instance.save()
            return instance