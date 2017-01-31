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

team1 = SoccerTeam(name="team1",login="etu1")
team1.add("SOLO",MS.Defense())

joueur2 = Player("Attaquant", MS.Attack())
joueur3 = Player("Defenseur", MS.Defense())
team2 = SoccerTeam("Equipe 2", [joueur2,joueur3])
