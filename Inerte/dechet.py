import pygame, random
from objet import *

class dechet(Objet):
    def __init__(self,energie,position):
        Objet.__init__(self, energie, position)
        self.name = "dechet"
        self.position=position
        
    
    #sprite
    def draw(self, position, i):
        gifNumber='./sprite/Cacs/frame-'+str(i%5+1)+'.gif'
        image = pygame.image.load(gifNumber)
        screen.blit(image, position)
        
