from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Attending_athlete
from .serializers import Attending_athleteSerializer
from django.contrib.auth.models import User

class Attending_athleteList(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):
        sports = Attending_athlete.objects.all()
        serializer = Attending_athleteSerializer(sports, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Attending_athleteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
