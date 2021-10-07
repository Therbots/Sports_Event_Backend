from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'user_id', 'street', 'city', 'state', 'zipcode']

        def create(self, validated_data):
            return Location.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.street = validated_data.get('street', instance.street)
            instance.city = validated_data.get('city', instance.city)
            instance.zipcode = validated_data.get('zipcode', instance.zipcode)
            instance.save()
            return instance