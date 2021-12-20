import pygame
from objet import *

class beef(Objet):
    def __init__(self,vie,position):
        Objet.__init__(self,vie, position)
        self.vitesse=0 #vitesse en fonction de l'énergie
        self.name = "viande"
        self.position=position
    
    #sprite du bled
    def draw(self, position, i):
        gifNumber='./sprite/steak/steak.png'
        image = pygame.image.load(gifNumber)
        screen.blit(image, position)
    