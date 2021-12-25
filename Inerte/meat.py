import pygame
from object import *

class Beef(Object):
    def __init__(self,energy,position):
        Object.__init__(self,energy, position)
        self.name = "meat"
        self.position = position
        self.attack = 0
    
    #sprite
    def draw(self, position, i):
        gifNumber ='./sprite/steak/steak.png'
        image = pygame.image.load(gifNumber)
        screen.blit(image, position)
