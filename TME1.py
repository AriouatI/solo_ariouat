# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
import math
import toolbox

#Coordonnees cartesiennes
v = Vector2D(1.,1.)
# Coordonnees polaires
w = Vector2D(angle=3.14/2,norm=1)
#Vecteur aleatoire
z = Vector2D.create_random(-0.5,0.5)
#ou retire le vecteur aleatoirement
v.random(-1,1)
#Operations usuelles
print v+w, v-w, 2*v, v/2,
#Manipulation (+=, -=, *=, /=)
v += w
v.x += 1
v.norm += 1
v.angle += 1
print v
# norme, distance, produit scalaire
print v.norm, v.distance(w), v.dot(w)
#Normalisation, norme max, mise a l echelle
v.scale(2)
print v
v.normalize()
print v
print v.norm_max(0.2)
# Attention, normalize et scale change le vecteur
# norm_max renvoie un autre vecteur
        
class MyStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma strat")
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        adv_but=Vector2D(settings.GAME_WIDTH/2+(-1)**(mystate.key[0]+1)*settings.GAME_WIDTH/2,settings.GAME_HEIGHT/2)
        if mystate.can_shoot():
            return mystate.shoot(adv_but)
        return mystate.aller(mystate.ball_position())   
        
class MyStrategy1(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma strat")
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        but=Vector2D(settings.GAME_WIDTH/2+(-1)**(mystate.key[0])*settings.GAME_WIDTH/2,settings.GAME_HEIGHT/2)
        adv_but=Vector2D(settings.GAME_WIDTH/2+(-1)**(mystate.key[0]+1)*settings.GAME_WIDTH/2,settings.GAME_HEIGHT/2)
        if mystate.can_shoot():
            return mystate.shoot(adv_but)
        elif mystate.my_position().distance(mystate.ball_position())<40:
            return mystate.aller(mystate.ball_position())
        return mystate.aller((mystate.ball_position()-but).normalize()*10+but)   
#Vector2D(settings.GAME_WIDTH/2+(-1)**(mystate.key[0])*60,settings.GAME_HEIGHT/2)
joueur1 = Player("joueur 1", MyStrategy())
joueur2 = Player("joueur 2", MyStrategy1())
print joueur1.name, joueur2.strategy, joueur2.name, joueur2.strategy
team1 = SoccerTeam("Equipe 1", [joueur1, joueur2])
# nombre de joueurs de l equipe
print(team1.nb_players)
# renvoie la liste des noms, la liste des strategies
print(team1.players_name, team1.strategies)
# nom et strategie du premier joueur
print team1.player_name(0), team1.strategy(0)

joueur3 = Player("joueur 3", MyStrategy())
joueur4 = Player("joueur 4", MyStrategy1())

team2 = SoccerTeam("Equipe 2", [joueur3, joueur4])
# nombre de joueurs de l equipe
print(team1.nb_players)
# renvoie la liste des noms, la liste des strategies
print(team1.players_name, team1.strategies)
# nom et strategie du premier joueur
print team1.player_name(0), team1.strategy(0)

#Creer un match entre 2 equipes et de duree 2000 pas
match = Simulation(team1, team2, 2000)
#Jouer le match (sans le visualiser)
#match.play()
#Jouer le match en le visualisant
#show_simu(match)
#Attention !! une fois le match joue, la fonction play() permet de faire jouer le replay
# mais pas de relancer le match !!!
# Pour regarder le replay d un match
show_simu(match)
# Pour reinitialiser un match
match.reset()

