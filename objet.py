listeDesViandes=[]
listeDesDechets=[]

import pygame, random
SCREENWIDTH=800
SCREENHEIGHT=600
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

class Objet:
    def __init__(self,energie):
        self.energie=energie

    def inZone(self,rayon,objectPosition):#check si la distance entre 2 objets est inférieur à une rayon donné 
        pass

    def manger(self,proie):#tout les être vivants mangent
        pass