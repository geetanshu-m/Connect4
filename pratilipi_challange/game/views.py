from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, status
import uuid
from pratilipi_challange.game.models import (
    users,
    userGame,
    gameMoves
)
from pprint import pprint

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
                userId = users.objects.get(userId=request.data['token'])
                userGame.objects.filter(userId=userId, finished=0).update(finished=1)
                gameId = userGame.objects.create(**{
                    "userId":userId,
                })
                return Response({
                    "message":"Started a new game",
                    "gameId":gameId.id
                }, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({
                        "message":"Invalid token ID",
                        "error":str(e)
                    }, status=status.HTTP_204_NO_CONTENT)
        
        user_token = str(uuid.uuid1())

        user = users.objects.create(userId=user_token)
        gameId = userGame.objects.create(**{
            "userId":user,
        })

        return Response({
            "user_token":user_token,
            "game_token":gameId.id,
            "message":"Started a new game, keep the token safe"
        }, status=status.HTTP_200_OK)

# def checkWin(matrix):


def validateMoves(userGameId, columnNew, colour):

    if columnNew>6:
        return False
    columnNew -= 1
    gameMovesObjs = gameMoves.objects.filter(userGameId=userGameId)
    
    matrix = []
    for i in range(6):
        matrix.append([])
        for _ in range(7):
            matrix[i].append(0)

    for x in gameMovesObjs:
        column = int(x.column)
        row = x.row
        color = x.colour
        matrix[row][column] = color
    
    color = -1 if colour == "red" else 1
    print(colour, color)
    breaked = 1
    for x in list(range(5,-1,-1)):
        if matrix[x][columnNew] == 0:
            gameMoves.objects.create(**{
                "userGameId":userGameId,
                "column":columnNew,
                "row":x,
                "colour":color
            })
            breaked = 0
            break
    pprint(matrix)
    if breaked:
        return False
    return True

@api_view(['POST'])
def makeMove(request):
    if request.method == "POST":
        if "user_token" not in request.data:
            return Response({
                "message":"userToken not present"
            })
        if "column" not in request.data:
            return Response({
                "message":"Column not present"
            })
        if "color" not in request.data:
            return Response({
                "message":"Colour not present"
            })
        try:
            user = users.objects.get(userId=request.data['user_token'])
        except Exception as e:
            return Response({
                    "message":"Invalid user token ID",
                    "error":str(e)
                }, status=status.HTTP_204_NO_CONTENT)
        try:
            userGameId = userGame.objects.get(userId=user,finished=0)
        except Exception as e:
            return Response({
                "message":"Invalid Game ID, try creating new game",
                "error":str(e)
            })
        if validateMoves(
            userGameId, 
            request.data['column'],
            request.data['color']
            ):
            return Response({
                "message":"Valid Moves"
            })
        else:
            return Response({
                "message":"Invalid Moves"
            })
        
