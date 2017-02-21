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
    return m.aller(m.ballPredict(1))
    
def intercepter(m,d):
    return m.aller((m.ball_position()-m.my_but).normalize()*d+m.my_but)
    
def saligner(m,d):
    return m.aller((m.ball_position()-m.adv_but).normalize()*d+m.adv_but)
    
def shootToGoal(m):
    return m.shoot(m.adv_but)


def shootEnA(m):
    if (m.ball_position().y<=settings.GAME_HEIGHT/2):
        return m.shoot(m.posA-Vector2D(0,settings.GAME_HEIGHT/4))
    if (m.ball_position().y>=settings.GAME_HEIGHT/2):
        return m.shoot(m.posA+Vector2D(0,settings.GAME_HEIGHT/4))
  
def allerEnA(m):
    if (m.ball_position().y<settings.GAME_HEIGHT/2):
        return m.aller(m.posA-Vector2D(0,settings.GAME_HEIGHT/4))
    if (m.ball_position().y>settings.GAME_HEIGHT/2):
        return m.aller(m.posA+Vector2D(0,settings.GAME_HEIGHT/4))

def goToBallAmeliore(m,k):
    return m.aller(m.ball_position(),k*m.distanceToBall(m.my_position()))
 
def shootToGoalAmeliore(m,k):
    return m.shoot(m.adv_but,k)

def degager(m):
    if m.can_shoot():
        return shootEnA(m)
    return goToBall(m)

def tirer(m):
    if m.can_shoot():
        return shootToGoal(m)
    return goToBall(m)
    
def dribler(m):
    if m.can_shoot():
        return shootToGoalAmeliore(m,0.5)
    return goToBall(m)