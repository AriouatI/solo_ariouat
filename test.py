# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import math
import toolbox
import briques as BDB
import messtrategies as MS

from soccersimulator import settings,SoccerTeam, Simulation, show_simu, KeyboardStrategy
from soccersimulator import Strategy, SoccerAction, Vector2D, load_jsonz,dump_jsonz,Vector2D
import logging
import sys
import pickle
from arbres import *
from arbres_utils import build_apprentissage,affiche_arbre,DTreeStrategy
from sklearn.tree import export_graphviz
from sklearn.tree import DecisionTreeClassifier

team1=SoccerTeam("team1")
team2=SoccerTeam("team2")
"""
team1.add("ATTAQUANT 1", MS.Attack3())
team1.add("ATTAQUANT 2 ", MS.Intercept())
team1.add("DEFENSEUR 1", MS.DefenseBase())
team1.add("DEFENSEUR 2", MS.Attack2())

team2.add("ATTAQUANT 1", MS.Attack3())
team2.add("ATTAQUANT 2 ", MS.Intercept())
team2.add("DEFENSEUR 1", MS.DefenseBase())
team2.add("DEFENSEUR 2", MS.Attack2())

simu = Simulation(team1,team2,3000)
show_simu(simu)
"""

KBStrat=KeyboardStrategy()
KBStrat.add('a',MS.Tirer())
KBStrat.add('z',MS.Degager())
KBStrat.add('e',MS.Dribbler())
KBStrat.add('r',MS.Intercepter())

KBStrat.add('h',MS.AllerAGauche())
KBStrat.add('k',MS.AllerADroite())
KBStrat.add('j',MS.AllerEnBas())
KBStrat.add('u',MS.AllerEnHaut())

team1.add("Manuel1", KBStrat)
#team1.add("Manuel2", MS.DefenseBase())

team2.add("Auto1",MS.Attack2())
#team2.add("Auto2", MS.Intercept())

simu = Simulation(team1,team2,1000)
"""
show_simu(simu)
training_states = KBStrat.states
dump_jsonz(training_states,"game12.jz")
"""

    
states_tuple = load_jsonz("game11.jz")+load_jsonz("yannick.jz")+load_jsonz("game2.jz")+load_jsonz("game3.jz")+load_jsonz("game10.jz")+load_jsonz("game9.jz")+load_jsonz("game4.jz")+load_jsonz("game5.jz")+load_jsonz("game8.jz")+load_jsonz("game6.jz")+load_jsonz("game7.jz")
data_train, data_labels = build_apprentissage(states_tuple,mes_params)
dt = apprend_arbre(data_train,data_labels,depth=10)
affiche_arbre(dt)
genere_dot(dt,"test_arbre.dot")
pickle.dump(dt,open("tree.pkl","wb"))

dtree = pickle.load(open(os.path.join(os.path.dirname(__file__),"tree.pkl"),"rb"))
dic = {"Dribbler":MS.Dribbler(),"Tirer":MS.Tirer(),"Degager":MS.Degager(),"Intercepter":MS.Intercept(),"Saligner":MS.Saligner()}
treeStrat1 = DTreeStrategy(dtree,dic,MS.mes_params)
treeStrat2 = DTreeStrategy(dtree,dic,mes_params)
team3 = SoccerTeam("Arbre Team")
#team3.add("Joueur 1",treeStrat1)
team3.add("Arbre",treeStrat1)
simu = Simulation(team3,team2)
show_simu(simu)
