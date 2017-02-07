# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 18:35:21 2017

@author: 3305496
"""
from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
import math
import toolbox
import briques as BDB

class Attack(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma strat")
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        if mystate.can_shoot():
            return BDB.shootToGoal(mystate)
        return BDB.goToBall(mystate)

class Defense(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma strat")
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        if mystate.can_shoot():
            return BDB.shootToGoal(mystate)
        elif mystate.my_position().distance(mystate.ball_position())<40:
            return BDB.goToBall(mystate)
        return BDB.intercepter(mystate,10)

class Defense2(Strategy):
    def __init__(self):
        self.enplace=0
        Strategy.__init__(self,"Ma strat")
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        if mystate.can_shoot():
            if (mystate.closest(4)[0] and self.enplace==0):
                self.enplace=1
                return BDB.saligner(mystate,mystate.distanceToBall(mystate.adv_but)+2)
            self.enplace=0
            return BDB.shootToGoal(mystate)
        elif mystate.my_position().distance(mystate.ball_position())<40:
            return BDB.goToBall(mystate)
        return BDB.intercepter(mystate,10)

class Intercept(Strategy):
    def __init__(self):
        self.enplace=0
        Strategy.__init__(self,"Ma strat")      
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        if mystate.can_shoot():
            if (mystate.closest(4)[0] and self.enplace==0):
                self.enplace=1
                return BDB.saligner(mystate,mystate.distanceToBall(mystate.adv_but)+2)
            self.enplace=0
            return BDB.shootToGoal(mystate)
        if (not mystate.closest(0)[0] or mystate.closest(0)[1]!=idplayer): 
            return BDB.intercepter(mystate,mystate.distanceToBall(mystate.my_but)*0.65)
        return BDB.goToBallPredict(mystate)

class Attack2(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma strat")
        self.enplace=0
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        if mystate.can_shoot():
            if (mystate.closest(4)[0] and self.enplace==0):
                self.enplace=1
                return BDB.saligner(mystate,mystate.distanceToBall(mystate.adv_but)+2)
            self.enplace=0
            return BDB.shootToGoal(mystate)
        if (mystate.closest(0)[0] and mystate.closest(0)[1]!=idplayer):
                return BDB.saligner(mystate,mystate.distanceToBall(mystate.adv_but)-30)
        return BDB.goToBall(mystate)

class DefenseurQuiVaPasLoin(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma strat")
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        if mystate.can_shoot():
		return BDB.shootToGoal(mystate)
        elif mystate.ball_position().x<90:
            	return BDB.goToBall(mystate)
        return BDB.intercepter(mystate,10)
        
"""
class Def1(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma strat")
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        if mystate.can_shoot():
            return BDB.shootToGoal(mystate)
        elif mystate.my_position().distance(mystate.ball_position())<45 and mystate.ball_position().x<75:
            return BDB.goToBall(mystate)
        return BDB.intercepter(mystate,10)

class AttaquantQuiAttend(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma strat")
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        a=state.step
        if (a<40):
            return Strategy()
        if mystate.can_shoot():
            return BDB.shootToGoal(mystate)
        return BDB.goToBall(mystate)



class Shadow(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma strat")
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        if mystate.can_shoot():
            return BDB.shootToGoal(mystate)
        return mystate.aller(mystate.advPos(0)) 
"""
