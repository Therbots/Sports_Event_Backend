from rest_framework import serializers
from .models import Skill_level

class Skill_levelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill_level
        fields = ['id', 'user_id', 'sport', 'level']

        def create(self, validated_data):
            return Skill_level.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.level = validated_data.get('level', instance.level)
            instance.save()
            return instance
