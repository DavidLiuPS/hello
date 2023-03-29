"""tennis_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
#from django.contrib import admin
#from django.urls import path

#urlpatterns = [
#    path('admin/', admin.site.urls),
#]

#urls.py
'''
from django.conf import settings
from django.contrib import admin
from django.urls import path
#from django.utils import timezone

def players_api(request):
    #Score should be as a string
    players_score = {"player_1":0, "player_2":2}
    return players_score

def players_api(request):
    #Score should be as a string
    players_score = {"player_1":0, "player_2":2}
    #Now display the scores:
    if players_score["player_1"] == 3 and players_score["player_2"] == 3:
        #Deuce
    return players_score

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/players/', players_api),
]
'''

# time_api/urls.py
from django.conf import settings
from django.contrib import admin
from django.http import JsonResponse
from django.urls import path
#from django.utils import timezone
import argparse
import random
import numpy as np

def player1_api(request):
    return player1_score

def player2_api(request):
    return player1_score

SCORE_MAPPINGS = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

def play_game(player1_score, player2_score):
    Deuce = "Deuce"
    Advantage = "Advantage"
    if player1_score == 3 and player2_score == 3:
        return (Deuce, Deuce, False)

    if player1_score <= 3 and player2_score <= 3:
        return (SCORE_MAPPINGS[player1_score], SCORE_MAPPINGS[player2_score], False)

    else:
        if (player1_score - player2_score >= 2):
            return ("Winner", "Loser", True)
        if (player2_score - player1_score >= 2):
            return ("Loser", "Winner", True) 
        #Going back to Deuce
        if player1_score == player2_score:
            return (Deuce, Deuce, False)
        if (player1_score > player2_score):
            return (Advantage, Deuce, False)
        if (player2_score > player1_score):
            return (Deuce, Advantage, False) 

def main():
    #Generate skill levels as decimals.
    player_1_skill = random.uniform(0,1)
    player_2_skill = random.uniform(0,1)

    player_1_name = "Prem Pant"
    player_2_name = "Lachie Pring"

    players_skill = {player_1_name: player_1_skill, player_2_name: player_2_skill}
    players_points = {player_1_name: 0, player_2_name: 0}

    print(players_skill)
    #Probability player 1 wins the point
    player_1_percentage = player_1_skill/(player_1_skill + player_2_skill)
    endgame = False
    while endgame == False:
        #Bernoulli distribution with parameter player_1_percentage
        outcome = np.random.binomial(size=1, n=1, p=player_1_percentage)
        if outcome == 1:
            players_points[player_1_name] += 1
        else:
            players_points[player_2_name] += 1
        #Now check whether the game is over
        ret = play_game(players_points[player_1_name], players_points[player_2_name])
        if ret[2] == True:
            print("{p1name}: {p1score}, {p2name}: {p2score}".format(p1name = player_1_name, 
                p1score = ret[0], p2name = player_2_name, p2score = ret[1]))
            endgame = True
        else:
            print("{p1name}: {p1score}, {p2name}: {p2score}".format(p1name = player_1_name, 
                p1score = ret[0], p2name = player_2_name, p2score = ret[1]))

main()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/player1/', player1_api),
    path('api/player2/', player2_api),
]


if __name__ == "__main__":
    parser = argparse.ArgumentParser("main")
