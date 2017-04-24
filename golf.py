from soccersimulator import GolfState,Parcours1,Parcours2,Parcours3,Parcours4
from soccersimulator import SoccerTeam,show_simu
from soccersimulator import Strategy,SoccerAction,Vector2D,settings
import toolbox as tb
import briques as BDB

GOLF = 0.001
SLALOM = 10.


class FonceStrategy(Strategy):
    def __init__(self):
        super(FonceStrategy,self).__init__("Demo")
    def compute_strategy(self,state,id_team,id_player):
        mystate = tb.MyState(state,id_team,id_player)
        """ zones : liste des zones restantes a valider """
        zones = state.get_zones(id_team)
        if len(zones)==0:
            """ shooter au but """
            return BDB.shootToGoal(mystate)
            #SoccerAction(state.ball.position-state.player_state(id_team,id_player).position,\Vector2D((2-id_team)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)-state.ball.position)
        """ zone : carre de zone avec z.position angle bas,gauche et z.l longueur du cote
            centre du carre : zone.position+Vector2D(z.l/2.,z.l/2.)
            zone.dedans(point) : teste si le point est dans la zone
        """
        zone = mystate.closestZone(zones)
        """ si la ball est dans une zone a valider """
        if zone.dedans(state.ball.position):
            return BDB.shootToZone(mystate,zone,0.00001)
        if (mystate.distanceToZone(zone.position.norm)<40):
            return BDB.dribblerToZone(mystate,zone,0.7)
        return BDB.shootToZone(mystate,zone,6)
        """ 
        distance = state.player_state(id_team,id_player).position.distance(zone.position+Vector2D(zone.l/2,zone.l/2))
        return SoccerAction()
        """
class slalom(Strategy):
    def __init__(self):
        super(slalom,self).__init__("Demo")
    def compute_strategy(self,state,id_team,id_player):
        mystate = tb.MyState(state,id_team,id_player)
        """ zones : liste des zones restantes a valider """
        zones = state.get_zones(id_team)
        if len(zones)==0:
            """ shooter au but """
            return BDB.shootToGoal(mystate)
            #SoccerAction(state.ball.position-state.player_state(id_team,id_player).position,\Vector2D((2-id_team)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)-state.ball.position)
        """ zone : carre de zone avec z.position angle bas,gauche et z.l longueur du cote
            centre du carre : zone.position+Vector2D(z.l/2.,z.l/2.)
            zone.dedans(point) : teste si le point est dans la zone
        """
        zone = mystate.closestZone(zones)
        """ si la ball est dans une zone a valider """
        if zone.dedans(state.ball.position):
            zone = mystate.closestZone(zones)
            return BDB.shootToZone(mystate,zone,20)
        """if (mystate.distanceToZone(zone.position.norm)<40):
            return BDB.dribblerToZone(mystate,zone,0.7)"""
        return BDB.shootToZone(mystate,zone,9)
        
class DefenseBase(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Ma strat")
    def compute_strategy(self,state,id_team,id_player):
        mystate = tb.MyState(state,id_team,id_player)
        zones = state.get_zones(id_team)
        zone = mystate.closestZone(zones)
        if mystate.can_shoot():
            if len(zones)==0:
                return BDB.shootToGoal(mystate)
            zone = mystate.closestZone(zones)
            return BDB.shootToZone(mystate,zone,20)
        elif (mystate.my_position().distance(mystate.ball_position())<40 and mystate.my_but.distance(mystate.ball_position())<90):
            return BDB.goToBallPredict(mystate)
        if len(zones)==0:   
            return BDB.intercepter(mystate,20)
        zone = mystate.closestZone(zones)
        return BDB.shootToZone(mystate,zone,20)


team1 = SoccerTeam()
team2 = SoccerTeam()
team1.add("John",slalom())
team1.add("John",DefenseBase())

team2.add("John",FonceStrategy())
"""
simu = Parcours1(team1=team1,vitesse=GOLF)
show_simu(simu)

simu = Parcours2(team1=team1,vitesse=GOLF)
show_simu(simu)
simu = Parcours3(team1=team1,vitesse=SLALOM)
show_simu(simu)"""

simu = Parcours4(team1=team1,team2=team2,vitesse=SLALOM)
show_simu(simu)
