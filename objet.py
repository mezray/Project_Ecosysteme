listeDesViandes=[]
listeDesDechets=[]

import pygame, random
SCREENWIDTH=800
SCREENHEIGHT=600
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

class Objet:
    def __init__(self,energie,vie,sexe):
        self.energie=energie
        self.vie=vie
        self.sexe=sexe

    def reproduire(self):#tout les être vivants savent reproduire
        pass

    def inZone(self,rayon,objectPosition):#check si la distance entre 2 objets est inférieur à une rayon donné 
        distance= ((self.position[0]-objectPosition[0])**2+(self.position[1]-objectPosition[1])**2)**0.5#pygame.sprit.collide_cercle
        if distance==0.0:
            return False
        if distance<=rayon:
            return True
        return False

    def manger(self,proie):#tout les être vivants mangent
        pass