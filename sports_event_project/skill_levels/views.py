from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Skill_level
from .serializers import Skill_levelSerializer
from django.contrib.auth.models import User

class Skill_levelList(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):
        sports = Skill_level.objects.all()
        serializer = Skill_levelSerializer(sports, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Skill_levelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
