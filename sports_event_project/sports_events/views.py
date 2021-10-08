from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Sports_event
from .serializers import Sports_eventSerializer
from django.contrib.auth.models import User

# class Sports_eventList(APIView):

#     permission_classes = [IsAuthenticated]

#     def get(self,request):
#         sports_events = Sports_event.objects.all()
#         serializer = Sports_eventSerializer(sports_events, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = Sports_eventSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_events(request):
    sports_event = Sports_event.objects.all()
    serializer = Sports_eventSerializer(sports_event, many=True)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_sports_events(request):
    if request.method == 'POST':
        serializer = Sports_eventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        sports_event = Sports_event.objects.filter(user_id=request.user.id)
        serializer = Sports_eventSerializer(sports_event, many=True)
        return Response(serializer.data)
# Create your views here.
