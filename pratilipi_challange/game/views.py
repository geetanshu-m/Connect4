from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, status


@api_view(['GET'])
def Game(request):
    if request.method == "GET":
        return Response({
            "message":"Hello World from the Game"
        }, status=status.HTTP_200_OK)