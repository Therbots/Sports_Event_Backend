from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Favorite_sport
from .serializers import Favorite_sportSerializer, Favorite_sportsSerializer
from django.contrib.auth.models import User

# class Favorite_sportList(APIView):

#     permission_classes = [IsAuthenticated]

#     def get(self,request):
#         favorite_sports = Favorite_sport.objects.all()
#         serializer = Favorite_sportSerializer(favorite_sports, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = Favorite_sportSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_favorite_sports(request):
    if request.method == 'POST':
        serializer = Favorite_sportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        favorite_sports = Favorite_sport.objects.filter(user_id=request.user.id)
        serializer = Favorite_sportsSerializer(favorite_sports, many=True)
        return Response(serializer.data)
# Create your views here.
