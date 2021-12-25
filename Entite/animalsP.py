import pygame
from plant import *

class Banana(Plant):
    def __init__(self,energy,health,radiusRacine,radiusSemis,position):
        Plant.__init__(self,radiusRacine,radiusSemis)
        Living.__init__(self,energy,health,sex='')
        self.name = "banana"
        self.strength = 5
        self.position = position
    
    #sprite
    def draw(self, position, i):
        gifNumber ='./sprite/banana/frame-'+str(i+1)+'.gif'
        image = pygame.image.load(gifNumber)
        screen.blit(image, position)

p=100
while p < 50:
    banana1=Banana(150,10,300,100,position=[random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)])
    listeDesPlantes.append(banana1)
    p+=1 