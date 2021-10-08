from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Competitiveness_level
from .serializers import Competitiveness_levelSerializer
from django.contrib.auth.models import User

# class Competitiveness_levelList(APIView):
    
#     permission_classes = [IsAuthenticated]

#     def get(self,request):
#         competitiveness_levels = Competitiveness_level.objects.all()
#         serializer = Competitiveness_levelSerializer(competitiveness_levels, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = Competitiveness_levelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_competitiveness_level(request):
    if request.method == 'POST':
        serializer = Competitiveness_levelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        competitiveness_level = Competitiveness_level.objects.filter(user_id=request.user.id)
        serializer = Competitiveness_levelSerializer(competitiveness_level, many=True)
        return Response(serializer.data)

# Create your views here.
