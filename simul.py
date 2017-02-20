# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 18:32:37 2017

@author: 3671626
"""

from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
import toolbox
import briques as BDB
import messtrategies as MS
import pyglet

class Attack(Strategy):
    def __init__(self,i,j,k):
        Strategy.__init__(self,"Ma strat")
        self.i=i
        self.j=j
        self.k=k
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        if mystate.can_shoot():
            return BDB.shootToGoalAmeliore(mystate,self.j,self.k)
        return BDB.goToBallAmeliore(mystate,self.i)
                    

state = SoccerState.create_initial_state(1,1)
state.player_state(1,0).position = Vector2D(75,45)
state.ball.position = Vector2D(90,45)

team2=SoccerTeam("Immobile")
team2.add("IMMO",Strategy("base"))

l=[]
for i in range (1,10+1):
    print(i)
    for j in range(1,10+1):
        for k in range(1,10+1):
            l.append([i/10.,j/10.,k/10.,1])

for j in range (1,5):
    for i in range (len(l)):
        team1=SoccerTeam("Ariouati")
        team1.add("ATTAQUANT", Attack(l[i][0],l[i][1],l[i][2]))
        match = Simulation(team1, team2,50,initial_state=state)
        match.start()
        if (match.get_score_team(1)==0 and l[i][3]==1):
            l[i][3]=0
        match.reset()

for i in range (len(l)):
    if (l[i][3]==1):
        print(l[i])

