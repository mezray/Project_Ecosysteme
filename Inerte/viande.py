import pygame
from objet import *

class beef(Objet):
    def __init__(self,energie,vie,sexe,rayonVision,rayonContact,position=[100,100]):
        Objet.__init__(self,energie,vie,sexe)
        self.vitesse=0 #vitesse en fonction de l'énergie
        self.name = "viande"
        self.position=position
        self.attaque = self.energie
    
    #sprite du bled
    def draw(self, position, i):
        if i == 0:
            image = pygame.image.load("./sprite/pug/frame-1.gif")
            screen.blit(image, position)
        if i == 1:
            image = pygame.image.load("./sprite/pug/frame-2.gif")
            screen.blit(image, position)
        if i == 2:
            image = pygame.image.load("./sprite/pug/frame-3.gif")
            screen.blit(image, position)
        if i == 3:
            image = pygame.image.load("./sprite/pug/frame-4.gif")
            screen.blit(image, position)
