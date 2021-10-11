from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Profile
from .serializers import ProfileSerializer
from django.contrib.auth.models import User

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
def user_profile(request):
    if request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        profiles = Profile.objects.filter(user_id=request.user.id)
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
