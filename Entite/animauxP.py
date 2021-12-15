import pygame
from plante import *

class rose(Plante):
    def __init__(self,energie,vie,rayonRacine,rayonSemis,position):
        Plante.__init__(self,rayonRacine,rayonSemis)
        Vivant.__init__(self,energie,vie,sexe='')
        self.name = "rose"
        self.position=position
    
    #sprite du bled
    def draw(self, position, i):
        gifNumber='./sprite/banana/frame-'+str(i+1)+'.gif'
        image = pygame.image.load(gifNumber)
        screen.blit(image, position)

p=0
while p < 10:
    enfant=rose(100,100,750,100,position=[random.randrange(0,750),random.randrange(0,550)])#self.__class__ permet de récupérer la classe de 'self'
    listeDesPlantes.append(enfant)
    p+=1 