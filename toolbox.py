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
#        self.my_but = ....
#        self.adv_but = ....
    def my_position(self):
        return self.state.player_state(self.key[0],self.key[1]).position
        #equivalent a self.player_state(self.key[0],self.key[1])
    def ball_position(self):
        return self.state.ball.position
    def aller(self,p):
        return SoccerAction(p-self.my_position(),Vector2D())
    def shoot(self,p):
        return SoccerAction(Vector2D(),p-self.my_position())
    def can_shoot(self):
        return self.my_position().distance(self.ball_position())<=(settings.PLAYER_RADIUS+settings.BALL_RADIUS)

#test
