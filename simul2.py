# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 11:06:08 2017

@author: 3671626
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
sys.path.append('../soccersimulator/examples/')
from arbres import *
from arbres_utils import build_apprentissage,affiche_arbre,DTreeStrategy
from sklearn.tree import export_graphviz
from sklearn.tree import DecisionTreeClassifier

logger = logging.getLogger("simuExpe")

class ShootSearch(object):
    """ nombre d'iterations maximales jusqu'a l'arret d'un round
        discr_step  : pas de discretisation du parametre
        nb_essais : nombre d'essais par parametre
    """
    MAX_STEP = 40
    def __init__(self):
        self.strat = ShootExpe()
        team1 = SoccerTeam("test")
        team1.add("Expe",self.strat)
        team2 = SoccerTeam("test2")
        team2.add("Nothing",Strategy())
        self.simu = Simulation(team1,team2,max_steps=40000)
        self.simu.listeners+=self
        self.discr_step = 20
        self.nb_essais = 1
    def start(self,visu=True):
        """ demarre la visualisation avec ou sans affichage"""
        if visu :
            show_simu(self.simu)
        else:
            self.simu.start()
    def begin_match(self,team1,team2,state):
        """ initialise le debut d'une simulation
            res : dictionnaire des Resultats
            last : step du dernier round pour calculer le round de fin avec MAX_STEP
            but : nombre de but pour ce parametre
            cpt : nombre d'essais pour ce parametre
            params : liste des parametres a tester
            idx : identifiant du parametre courant
        """
        self.res = dict()
        self.last = 0
        self.but = 0
        self.cpt = 0
        self.params = [x for x in  np.linspace(1,settings.maxPlayerShoot,self.discr_step)]
        self.idx=0

    def begin_round(self,team1,team2,state):
        """ engagement : position random du joueur et de la balle """
        position = Vector2D(np.random.random()*settings.GAME_WIDTH/2.+settings.GAME_WIDTH/2.,np.random.random()*settings.GAME_HEIGHT)
        self.simu.state.states[(1,0)].position = position.copy()
        self.simu.state.states[(1,0)].vitesse = Vector2D()
        self.simu.state.ball.position = position.copy()
        self.strat.norm = self.params[self.idx]
        self.last = self.simu.step
    def update_round(self,team1,team2,state):
        """ si pas maximal atteint, fin du tour"""
        if state.step>self.last+self.MAX_STEP:
            self.simu.end_round()
    def end_round(self,team1,team2,state):
        if state.goal>0:
            self.but+=1
        self.cpt+=1
        if self.cpt>=self.nb_essais:
            self.res[self.params[self.idx]] = self.but*1./self.cpt
            logger.debug("parametre %s : %f" %((str(self.params[self.idx]),self.res[self.params[self.idx]])))
            self.idx+=1
            self.but=0
            self.cpt=0
        """ si plus de parametre, fin du match"""
        if self.idx>=len(self.params):
            self.simu.end_match()

class ShootExpe(Strategy):
    def __init__(self,shoot=None):
        self.name = "simple action"
        self.norm = 0
    def compute_strategy(self,state,id_team,id_player):
        mystate = toolbox.MyState(state,id_team,id_player)
        return BDB.shootToGoal(mystate,self.norm)

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

team2.add("Auto1",MS.Attack())
#team2.add("Auto2", MS.Intercept())

simu = Simulation(team1,team2,3000)

expe = ShootSearch()
expe.start()
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
    f8=mystate.my_angle()
    return [f1,f2,f3,f4,f5,f6,f7,f8]
    
states_tuple = load_jsonz("2-0Attack.jz")
data_train, data_labels = build_apprentissage(states_tuple,mes_params)
dt = apprend_arbre(data_train,data_labels,depth=10)
affiche_arbre(dt)
genere_dot(dt,"test_arbre.dot")
pickle.dump(dt,open("tree.pkl","wb"))

dtree = pickle.load(open(os.path.join(os.path.dirname(__file__),"tree.pkl"),"rb"))
dic = {"Dribbler":MS.Dribbler(),"Tirer":MS.Tirer(),"Degager":MS.Degager(),"Intercepter":MS.Intercept(),"Saligner":MS.Saligner(),
       "Gauche":MS.AllerAGauche(),"Droite":MS.AllerADroite(),"Bas":MS.AllerEnBas(),"Haut":MS.AllerEnHaut()}
treeStrat1 = DTreeStrategy(dtree,dic,mes_params)
treeStrat2 = DTreeStrategy(dtree,dic,mes_params)
team3 = SoccerTeam("Arbre Team")
#team3.add("Joueur 1",treeStrat1)
team3.add("Joueur 2",treeStrat2)
simu = Simulation(team3,team2)


