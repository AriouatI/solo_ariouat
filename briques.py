# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 16:57:49 2017

@author: 3305496
"""

from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
import math
import toolbox

def goToBall(m):
	return m.aller(m.ball_position())
    
def goToBallPredict(m):
	return m.aller(m.ballPredict(5))
    
def intercepter(m,d):
	return m.aller((m.ball_position()-m.my_but).normalize()*d+m.my_but)
    
def saligner(m,d):
	return m.aller((m.ball_position()-m.adv_but).normalize()*d+m.adv_but)
    
def shootToGoal(m):
	return m.shoot(m.adv_but)
