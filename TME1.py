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
        
class MyStrategyAtt2(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma strat")
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        if mystate.can_shoot():
            return mystate.shoot(mystate.adv_but)
        return mystate.aller(mystate.ball_position())   
        
class MyStrategyDef1(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma strat")
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        if mystate.can_shoot():
            return mystate.shoot(mystate.adv_but)
        elif mystate.my_position().distance(mystate.ball_position())<45 and mystate.ball_position().x<75:
            return mystate.aller(mystate.ball_position())
        return mystate.aller((mystate.ball_position()-mystate.my_but).normalize()*10+mystate.my_but)

class MyStrategyDef2(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma strat")
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        if mystate.can_shoot():
            return mystate.shoot(mystate.adv_but)
        elif mystate.my_position().distance(mystate.ball_position())<45 and mystate.ball_position().x>75:
            return mystate.aller(mystate.ball_position())
        return mystate.aller((mystate.ball_position()-mystate.my_but).normalize()*10+mystate.my_but)

class MyStrategy2(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma strat")
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
	a=SoccerState.step
	b=SoccerState.step
	while (b<a+10):
		b+=1
        if mystate.can_shoot():
            return mystate.shoot(mystate.adv_but)
        return mystate.aller(mystate.ball_position())

class MyStrategyAtt1(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma strat")
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        if mystate.can_shoot():
            return mystate.shoot(mystate.adv_but)
        elif mystate.ball_position().x<90:
            return mystate.aller(mystate.ball_position())
        return mystate.aller((mystate.ball_position()-mystate.my_but).normalize()*10+mystate.my_but)

joueur1 = Player("Attaquant 1", MyStrategyAtt1())
joueur2 = Player("Defenseur 2", MyStrategyDef1())
#print joueur1.name, joueur2.strategy, joueur2.name, joueur2.strategy
team1 = SoccerTeam("Equipe 1", [joueur1, joueur2])

"""# renvoie la liste des noms, la liste des strategies
print(team1.players_name, team1.strategies)
# nom et strategie du premier joueur
print team1.player_name(0), team1.strategy(0)"""

joueur3 = Player("Defenseur 2", MyStrategyDef2())
joueur4 = Player("Attaquant 2", MyStrategyAtt2())
team2 = SoccerTeam("Equipe 2", [joueur3, joueur4])

#Creer un match entre 2 equipes et de duree 2000 pas
match = Simulation(team1, team2, 4000)
#Jouer le match (sans le visualiser)
#match.play()
#Jouer le match en le visualisant
show_simu(match)
#Attention !! une fois le match joue, la fonction play() permet de faire jouer le replay
# mais pas de relancer le match !!!
# Pour regarder le replay d un match
# show_simu(match)
# Pour reinitialiser un match
match.reset()

