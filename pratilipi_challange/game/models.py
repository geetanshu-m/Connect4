from django.db import models

# Create your models here.

class users(models.Model):
    userId = models.CharField(max_length=100)

    class Meta:
        db_table = "users"