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
sys.path.append('../soccersimulator/examples/')
from arbres import *
from arbres_utils import build_apprentissage,affiche_arbre,DTreeStrategy
from sklearn.tree import export_graphviz
from sklearn.tree import DecisionTreeClassifier

team1=SoccerTeam("team1")
team2=SoccerTeam("team2")

KBStrat=KeyboardStrategy()
KBStrat.add('a',MS.Tirer())
KBStrat.add('z',MS.Degager())
KBStrat.add('e',MS.Dribler())
KBStrat.add('q',MS.Intercepter())
KBStrat.add('h',MS.AllerAGauche())
KBStrat.add('k',MS.AllerADroite())
KBStrat.add('j',MS.AllerEnBas())
KBStrat.add('u',MS.AllerEnHaut())


team1.add("Sofiane", MS.Attack2())
team1.add("Ariouat", MS.Intercept())
team2.add("LI", MS.Attack2())
team2.add("Yannick", MS.DefenseBase())

simu = Simulation(team1,team2,3000)

show_simu(simu)
training_states = KBStrat.states
dump_jsonz(training_states,"infos_states.jz")
"""
def mes_params(state,idt,idp):
    mystate = toolbox.MyState(state,idt,idp)
    f1=mystate.distanceToBall(mystate.my_position())
    f2=int(mystate.imclosest())
    f3=int(mystate.mateclosest())
    f4=(mystate.my_position()-mystate.adv_but).norm
    return [f1,f2,f3,f4]
    
states_tuple = load_jsonz("infos_states.jz")
data_train, data_labels = build_apprentissage(states_tuple,mes_params)
dt = apprend_arbre(data_train,data_labels,depth=10)
affiche_arbre(dt)
genere_dot(dt,"test_arbre.dot")

dic = {"Dribler":MS.Dribler(),"Tirer":MS.Tirer(),"Degager":MS.Degager(),"Intercepter":MS.Intercept()}
treeStrat1 = DTreeStrategy(dt,dic,mes_params)
treeStrat2 = DTreeStrategy(dt,dic,mes_params)
team3 = SoccerTeam("Arbre Team")
team3.add("Joueur 1",treeStrat1)
team3.add("Joueur 2",treeStrat2)
simu = Simulation(team2,team3)
show_simu(simu)
"""
match.reset()
