from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Attending_athlete
from .serializers import Attending_athleteSerializer
from django.contrib.auth.models import User

# class Attending_athleteList(APIView):

#     permission_classes = [IsAuthenticated]

#     def get(self,request):
#         attending_athletes = Attending_athlete.objects.all()
#         serializer = Attending_athleteSerializer(attending_athletes, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = Attending_athleteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_attending_athlete(request):
    if request.method == 'POST':
        serializer = Attending_athleteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        attending_athlete = Attending_athlete.objects.filter(user_id=request.user.id)
        serializer = Attending_athleteSerializer(attending_athlete, many=True)
        return Response(serializer.data)
# Create your views here.
