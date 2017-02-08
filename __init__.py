# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 18:41:12 2017

@author: 3305496
"""

from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
import math
import toolbox
import briques as BDB
import messtrategies as MS

def get_team(i):
	s=SoccerTeam("Ariouati")
	if (i==1):
		s.add("SOLO",MS.Intecept())
	elif (i==2):
		s.add("ATTAQUANT", MS.Attack2())
		s.add("DEFENSEUR", MS.Intercept())
	elif (i==4):
		s.add("ATTAQUANT 1", MS.Attack2())
		s.add("ATTAQUANT 2 ", MS.Intercept())
		s.add("DEFENSEUR 1", MS.Defense())
		s.add("DEFENSEUR 2", MS.Attack())
	return s
    