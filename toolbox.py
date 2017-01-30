# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 16:42:54 2017

@author: 3671626
"""

from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
import math

class MyState(object):
    def __init__(self,state,idteam,idplayer):
        self.state = state
        self.key = (idteam,idplayer)
        self.my_but = Vector2D(settings.GAME_WIDTH/2+(-1)**(self.key[0])*settings.GAME_WIDTH/2,settings.GAME_HEIGHT/2) 
        self.adv_but = Vector2D(settings.GAME_WIDTH/2+(-1)**(self.key[0]+1)*settings.GAME_WIDTH/2,settings.GAME_HEIGHT/2)
    
    def my_position(self):
        return self.state.player_state(self.key[0],self.key[1]).position
        #equivalent a self.player_state(self.key[0],self.key[1])
    
    def opponentPosition(self):
        return (self.state.player_state((3-self.key[0]),0).position)
        
    def theOther(self):
        return (self.state.player_state((3-self.key[0]),1).position)
        
    def ball_position(self):
        return self.state.ball.position
    
    def aller(self,p):
        return SoccerAction(p-self.my_position(),Vector2D())
    
    def shoot(self,p):
        return SoccerAction(Vector2D(),p-self.my_position())
    
    def can_shoot(self):
        return self.my_position().distance(self.ball_position())<=(settings.PLAYER_RADIUS+settings.BALL_RADIUS)
    
    def distanceToBall(self,a):
        return (a-self.ball_position()).norm
        
    def closest2(self):
        goodSide=True
        maxid=self.key[1]
        maxi=self.distanceToBall(self.my_position())
        if (self.distanceToBall(self.opponentPosition())>=maxi):
            maxid=0
            goodSide=False
        if (self.distanceToBall(self.theOther())>=maxi):
            maxid=1
            goodSide=False
        return (goodSide,maxid)
        
    def closest1(self):
        goodSide=True
        maxid=self.key[1]
        maxi=self.distanceToBall(self.my_position())
        if (self.distanceToBall(self.opponentPosition())>=maxi):
            maxid=0
            goodSide=False
        return (goodSide,maxid)
