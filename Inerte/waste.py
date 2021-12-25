import pygame
from object import *

class Waste(Objet):
    def __init__(self,energy,position):
        Objet.__init__(self, energy, position)
        self.name = "waste"
        self.position = position
        
    
    #sprite
    def draw(self, position, i):
        gifNumber ='./sprite/Cacs/frame-'+str(i%5+1)+'.gif'
        image = pygame.image.load(gifNumber)
        screen.blit(image, position)
        
