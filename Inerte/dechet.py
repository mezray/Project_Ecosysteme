import pygame
from objet import *

class dechet(Objet):
    def __init__(self,vie, position):
        Objet.__init__(self, vie, position)
        self.vitesse=0 #vitesse en fonction de l'énergie
        self.name = "dechet"
        self.position=position
    
    #sprite du bled
    def draw(self, position, i):
        gifNumber='./sprite/Cacs/frame-'+str(i%5+1)+'.gif'
        image = pygame.image.load(gifNumber)
        screen.blit(image, position)
