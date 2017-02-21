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
        self.nbjoueurs=state.nb_players(1)
        self.my_but = Vector2D(settings.GAME_WIDTH/2+(-1)**(self.key[0])*settings.GAME_WIDTH/2,settings.GAME_HEIGHT/2) 
        self.adv_but = Vector2D(settings.GAME_WIDTH/2+(-1)**(self.key[0]+1)*settings.GAME_WIDTH/2,settings.GAME_HEIGHT/2)
        self.posA = Vector2D(settings.GAME_WIDTH/2+(-1)**(self.key[0]+1)**settings.GAME_WIDTH/2,settings.GAME_HEIGHT/2)
        self.coeff_Def=(-1)**(self.key[0]) # -1 si Equipe 1 sinon 1
        self.coeff_Att=(-1)**(self.key[0]+1) # 1 si Equipe 1 sinon -1

    def my_position(self):
        return (self.state.player_state(self.key[0],self.key[1]).position)
        
    def my_vitesse(self):
        return (self.state.player_state(self.key[0],self.key[1]).vitesse).norm
        
    def allierPos(self,i):
        return (self.state.player_state((self.key[0]),i).position)
    
    def advPos(self,i):
        return (self.state.player_state((3-self.key[0]),i).position)
        
    def ball_position(self):
        return self.state.ball.position
    
    def aller(self,p,k=6):
        return SoccerAction((p-self.my_position()).normalize()*k,Vector2D())
    
    def shoot(self,p,k=6):
        return SoccerAction(Vector2D(),(p-self.my_position()).normalize()*k)
    
    def can_shoot(self):
        return self.my_position().distance(self.ball_position())<=(settings.PLAYER_RADIUS+settings.BALL_RADIUS)
    
    def distanceToBall(self,a):
        return (a-self.ball_position()).norm
        
    def closest(self,m):
        mini=self.distanceToBall(self.my_position())
        goodSide=True
        maxid=self.key[1]        
        for i in range (self.nbjoueurs):
            if (self.distanceToBall(self.allierPos(i))<mini+m):
                mini=self.distanceToBall(self.allierPos(i))
                maxid=i
        for i in range (self.nbjoueurs):
            if (self.distanceToBall(self.advPos(i))<mini+m):
                mini=self.distanceToBall(self.advPos(i))
                maxid=i
                goodSide=False
        return (goodSide,maxid)
        
    def imclosest(self):
        return (self.closest(5)[0] and self.closest(5)[1]==self.key[1])
        
    def mateclosest(self):
        return (self.closest(5)[0] and self.closest(5)[1]!=self.key[1])

    def ballPredict(self,t):
        return self.ball_position()+(self.state.ball.vitesse)*t
