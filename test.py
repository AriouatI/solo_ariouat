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
import briques as BDB
import messtrategies as MS


joueur1 = Player("Sofiane", MS.Attack())
joueur2 = Player("messi", MS.Defense())
team1 = SoccerTeam("Equipe 1", [joueur1,joueur2])

joueur3 = Player("Li", MS.Intercept())
joueur4 = Player("Yannick", MS.Attack())
team2 = SoccerTeam("Equipe 2", [joueur3,joueur4])

"""
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("li",Defense())
team2.add("yannick",Attack())
"""
"""
#print joueur1.name, joueur2.strategy, joueur2.name, joueur2.strategy
# renvoie la liste des noms, la liste des strategies
print(team1.players_name, team1.strategies)
# nom et strategie du premier joueur
print team1.player_name(0), team1.strategy(0)
"""

#Creer un match entre 2 equipes et de duree 2000 pas
match = Simulation(team1, team2, 2000)
#Jouer le match (sans le visualiser)
#match.play()
#Jouer le match en le visualisant
show_simu(match)
#Attention !! une fois le match joue, la fonction play() permet de faire jouer le replay
# mais pas de relancer le match !!!
# Pour reinitialiser un match
match.reset()
