import pygame
from objet import *

class beef(Objet):
    def __init__(self,energie,position):
        Objet.__init__(self,energie, position)
        self.name = "viande"
        self.position=position
        self.attaque=0
    
    #sprite du bled
    def draw(self, position, i):
        gifNumber='./sprite/steak/steak.png'
        image = pygame.image.load(gifNumber)
        screen.blit(image, position)
    