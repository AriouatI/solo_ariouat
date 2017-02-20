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

class AttackBase(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma strat")
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        if mystate.can_shoot():
            return BDB.shootToGoal(mystate)
        return BDB.goToBall(mystate)

class DefenseBase(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma strat")
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        if mystate.can_shoot():
            return BDB.shootToGoal(mystate)
        elif (mystate.my_position().distance(mystate.ball_position())<40 and mystate.my_but.distance(mystate.ball_position())<90):
            return BDB.goToBall(mystate)
        return BDB.intercepter(mystate,20)

class Intercept(Strategy):
    def __init__(self):
        self.enplace=0
        Strategy.__init__(self,"Ma strat")      
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        if mystate.can_shoot():
            if (mystate.distanceToBall(mystate.my_but)<40):
                return BDB.shootToGoal(mystate)
            if (mystate.imclosest() and self.enplace==0):
                self.enplace=1
                return BDB.saligner(mystate,mystate.distanceToBall(mystate.adv_but)+2)
            self.enplace=0
            return BDB.shootToGoal(mystate)
        if ((mystate.imclosest()) or mystate.distanceToBall(mystate.my_but)<45):
            return BDB.goToBallPredict(mystate)
        return BDB.intercepter(mystate,mystate.distanceToBall(mystate.my_but)*0.65)

class Intercept2(Strategy):
    def __init__(self):
        self.enplace=0
        Strategy.__init__(self,"Ma strat")      
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        if mystate.can_shoot():
            if (mystate.distanceToBall(mystate.my_but)<40):
                return BDB.shootToGoal(mystate)
            if (mystate.imclosest() and self.enplace<3):
                self.enplace+=1
                return BDB.saligner(mystate,mystate.distanceToBall(mystate.adv_but)+2)
            if (mystate.imclosest() and self.enplace<5 and self.enplace>3):
                self.enplace+=1
                return BDB.saligner(mystate,mystate.distanceToBall(mystate.adv_but)+1)
            self.enplace=0
            return BDB.shootToGoal(mystate)
        if ((mystate.imclosest()) or mystate.distanceToBall(mystate.my_but)<45):
            return BDB.goToBallPredict(mystate)
        return BDB.intercepter(mystate,mystate.distanceToBall(mystate.my_but)*0.65)
        
        
class Intercept3(Strategy):
    def __init__(self):
        self.enplace=0
        Strategy.__init__(self,"Ma strat")      
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        if mystate.can_shoot():
            if (mystate.distanceToBall(mystate.my_but)<40):
                return BDB.shootEnA(mystate)
            if (mystate.imclosest() and self.enplace<3):
                self.enplace+=1
                return BDB.saligner(mystate,mystate.distanceToBall(mystate.adv_but)+2)
            if (mystate.imclosest() and self.enplace<5 and self.enplace>3):
                self.enplace+=1
                return BDB.saligner(mystate,mystate.distanceToBall(mystate.adv_but)+1)
            self.enplace=0
            return BDB.shootEnA(mystate)
        if ((mystate.imclosest()) or mystate.distanceToBall(mystate.my_but)<40):
            return BDB.goToBallPredict(mystate)
        return BDB.intercepter(mystate,mystate.distanceToBall(mystate.my_but)*0.65)

class Attack(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma strat")
        self.enplace=0
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        if mystate.can_shoot():
            if (mystate.imclosest() and self.enplace==0):
                self.enplace=1
                return BDB.saligner(mystate,mystate.distanceToBall(mystate.adv_but)+2)
            self.enplace=0
            return BDB.shootToGoal(mystate)
        if (mystate.mateclosest()):
            return BDB.saligner(mystate,mystate.distanceToBall(mystate.adv_but)-45)
        return BDB.goToBallPredict(mystate)
        
class Attack2(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma strat")
        self.enplace=0
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        if mystate.can_shoot():
            if (mystate.imclosest() and self.enplace<3):
                self.enplace+=1
                return BDB.saligner(mystate,mystate.distanceToBall(mystate.adv_but)+2)
            if (mystate.imclosest() and self.enplace<5 and self.enplace>3):
                self.enplace+=1
                return BDB.saligner(mystate,mystate.distanceToBall(mystate.adv_but)+1)
            self.enplace=0
            return BDB.shootToGoal(mystate)
        if (mystate.mateclosest()):
            return BDB.saligner(mystate,mystate.distanceToBall(mystate.adv_but)-45)
        return BDB.goToBallPredict(mystate)
        
class Attack3(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma strat")
        self.enplace=0
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        if mystate.can_shoot():
            if (mystate.imclosest() and self.enplace<3):
                self.enplace+=1
                return BDB.saligner(mystate,mystate.distanceToBall(mystate.adv_but)+2)
            if (mystate.imclosest() and self.enplace<5 and self.enplace>3):
                self.enplace+=1
                return BDB.saligner(mystate,mystate.distanceToBall(mystate.adv_but)+1)
            self.enplace=0
            return BDB.shootToGoal(mystate)
        if (mystate.mateclosest()):
            return BDB.allerEnA(mystate)
        return BDB.goToBallPredict(mystate)

class Solo(Strategy):
    def __init__(self):
        self.enplace=0
        Strategy.__init__(self,"Ma strat")      
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        if mystate.can_shoot():
            if (mystate.distanceToBall(mystate.my_but)<60):
                return BDB.shootToGoal(mystate)
            if (mystate.closest(2)[0] and self.enplace<3):
                self.enplace+=1
                return BDB.saligner(mystate,mystate.distanceToBall(mystate.adv_but)+2)
            if (mystate.closest(2)[0] and self.enplace<5 and self.enplace>3):
                self.enplace+=1
                return BDB.saligner(mystate,mystate.distanceToBall(mystate.adv_but)+1)
            self.enplace=0
            return BDB.shootToGoal(mystate)
        if (mystate.closest(0)[0] or mystate.distanceToBall(mystate.my_but)<60):
            return BDB.goToBallPredict(mystate)
        return BDB.intercepter(mystate,mystate.distanceToBall(mystate.my_but)*0.65)
        
class Solo1(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma strat")      
    def compute_strategy(self,state,idteam,idplayer):
        mystate = toolbox.MyState(state,idteam,idplayer)
        return BDB.degager(mystate)
        