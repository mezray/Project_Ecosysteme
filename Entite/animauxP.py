import pygame
from plante import *


class rose(Plante):
    def __init__(self,energie,vie,rayonRacine,rayonSemis,position):
        Plante.__init__(self,rayonRacine,rayonSemis)
        Vivant.__init__(self,energie,vie,sexe='')
        self.name = "rose"
        self.force = 5
        self.position=position
    
    #sprite
    def draw(self, position, i):
        gifNumber='./sprite/banana/frame-'+str(i+1)+'.gif'
        image = pygame.image.load(gifNumber)
        screen.blit(image, position)

p=0
while p < 50:
    enfant=rose(150,10,300,100,position=[random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)])#self.__class__ permet de récupérer la classe de 'self'
    listeDesPlantes.append(enfant)
    p+=1 