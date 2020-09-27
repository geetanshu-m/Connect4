from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, status
import uuid
from pratilipi_challange.game.models import users


@api_view(['POST'])
def Game(request):
    if request.method == "POST":

        return Response({
            "message":"Hello World from the Game",
            "token":str(uuid.uuid1())
        }, status=status.HTTP_200_OK)

@api_view(['POST'])
def startGame(request):
    if request.method == "POST":

        if "token" in request.data:
            try:
                users.objects.get(userId=request.data['token'])
                return Response({
                    "message":"Started a new game"
                }, status=status.HTTP_200_OK)
            except:
                return Response({
                        "message":"Invalid token ID"
                    }, status=status.HTTP_204_NO_CONTENT)
        
        new_token = str(uuid.uuid1())
        users.objects.create(userId=new_token)

        return Response({
            "token":new_token,
            "message":"Started a new game, keep the token safe"
        }, status=status.HTTP_200_OK)