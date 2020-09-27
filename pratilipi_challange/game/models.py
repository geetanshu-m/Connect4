from django.db import models
from django.utils import timezone

# Create your models here.

class users(models.Model):
    userId = models.CharField(max_length=100)
    createdAt = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "users"

class userGame(models.Model):
    userId = models.ForeignKey(users, on_delete=models.CASCADE, db_column='userId')
    createdAt = models.DateTimeField(default=timezone.now)
    # active = 0
    # finished = 1
    finished = models.IntegerField(default=0)
    # red = -1
    # yellow = 1
    # none = 0
    win = models.IntegerField(default=0)

    class Meta:
        db_table = "userGame"

class gameMoves(models.Model):
    userGameId = models.ForeignKey(userGame, on_delete=models.CASCADE, db_column='userGameId')
    createdAt = models.DateTimeField(default=timezone.now)
    column = models.IntegerField()
    row = models.IntegerField()
    colour = models.CharField(max_length=20)
    class Meta:
        db_table = "gameMoves"
