from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, parser_classes, permission_classes
from .models import Profile
from .serializers import ProfileSerializer
from django.contrib.auth.models import User
import requests
from rest_framework.parsers import MultiPartParser, FormParser

# class LocationList(APIView):

#     permission_classes = [IsAuthenticated]

#     def get(self,request):
#         locations = Location.objects.all()
#         serializer = LocationSerializer(locations, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = LocationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def user_profile(request, format=None):
    if request.method == 'POST':
        print(request.data)
        serializer = ProfileSerializer(data=request.data)
        street = request.data["street"]
        city = request.data["city"]
        state = request.data["city"]
        response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={street}{city}{state}&key=AIzaSyDxnPufIqzt-rlQ_chGZS38eYFrCAw8HNE')
        object = response.json()
        geo_location = object['results'][0]['geometry']
        lat = geo_location['location']['lat']
        lng = geo_location['location']['lng']
        if serializer.is_valid():
            serializer.save(user=request.user, lat=lat, lng=lng)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        profiles = Profile.objects.filter(user_id=request.user.id)
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
