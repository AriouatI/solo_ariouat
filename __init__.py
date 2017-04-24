# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 10:17:03 2017

@author: 3671626
"""
from soccersimulator import GolfState,Parcours1,Parcours2,Parcours3,Parcours4
import golf as G
from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
import math
import toolbox
import sys
import logging
import pickle
import os
import briques as BDB
import messtrategies as MS
from arbres_utils import DTreeStrategy
from sklearn.tree import export_graphviz
from sklearn.tree import DecisionTreeClassifier




def get_team(i):
    s=SoccerTeam("ASYL")
    if (i==1):
        s.add("golf",G.FonceStrategy())
    elif (i==2):
        s.add("slalom", G.slalom())
    elif (i==3):
        s.add("ATTAQUANT 1", G.DefenseBase())
        s.add("ATTAQUANT 2 ", G.slalom())

    return s
    