from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user_id', 'name', 'street', 'city', 'state', 'zipcode']

        def create(self, validated_data):
            return Profile.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.street = validated_data.get('street', instance.street)
            instance.city = validated_data.get('city', instance.city)
            instance.zipcode = validated_data.get('zipcode', instance.zipcode)
            instance.save()
            return instance