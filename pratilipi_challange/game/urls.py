from django.urls import path, include
from pratilipi_challange.game import views

urlpatterns = [
    path('', views.Game)
]