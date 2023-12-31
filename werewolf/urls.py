"""
URL configuration for werewolf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from game.views import *
from main.views import MainView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    path('game/new/', NewGameView.as_view(), name='new-game'),
    path('game/<int:id>/', GameView.as_view(), name='game'),
    path('game/<int:id>/start/', GameStart.as_view(), name='game-start'),
    path('game/<int:id>/round/<int:round>/', GameStart.as_view(), name='game-round'),
    path('game/<int:id>/round/<int:round>/vote/<int:pid>/', GameStart.as_view(), name='game-vote'),


]
