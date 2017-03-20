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
team1.add("Manuel2", Strategy())

team2.add("Auto1", Strategy())
team2.add("Auto2", Strategy())

simu = Simulation(team1,team2,9000)

show_simu(simu)
training_states = KBStrat.states
dump_jsonz(training_states,"infos_states.jz")

def mes_params(state,idt,idp):
    mystate = toolbox.MyState(state,idt,idp)
    f1=mystate.distanceToBall(mystate.my_position())
    f2=int(mystate.imclosest())
    f3=int(mystate.mateclosest())
    f4=(mystate.my_position()-mystate.adv_but).norm
    f5=int(mystate.ballmyside())
    f6=mystate.distanceToBall(mystate.my_but)
    f7=((mystate.key[0]-1)*settings.GAME_WIDTH)+mystate.my_position().x
    return [f1,f2,f3,f4,f5,f6,f7]
    
states_tuple = load_jsonz("infos_states.jz")
data_train, data_labels = build_apprentissage(states_tuple,mes_params)
dt = apprend_arbre(data_train,data_labels,depth=10)
affiche_arbre(dt)
genere_dot(dt,"test_arbre.dot")

dic = {"Dribbler":MS.Dribbler(),"Tirer":MS.Tirer(),"Degager":MS.Degager(),"Intercepter":MS.Intercept(),"Saligner":MS.Saligner(),
       "Gauche":MS.AllerAGauche(),"Droite":MS.AllerADroite(),"Bas":MS.AllerEnBas(),"Haut":MS.AllerEnHaut()}
treeStrat1 = DTreeStrategy(dt,dic,mes_params)
treeStrat2 = DTreeStrategy(dt,dic,mes_params)
team3 = SoccerTeam("Arbre Team")
team3.add("Joueur 1",MS.Intercept())
team3.add("Joueur 2",treeStrat2)
simu = Simulation(team3,team2)
show_simu(simu)
"""