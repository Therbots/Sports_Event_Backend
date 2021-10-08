from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Event_message_board
from .serializers import Event_message_boardSerializer
from django.contrib.auth.models import User

class Event_message_boardList(APIView):

    permission_classes = [IsAuthenticated]

    def get(self,request):
        sports = Event_message_board.objects.all()
        serializer = Event_message_boardSerializer(sports, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Event_message_boardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
