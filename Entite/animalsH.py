import pygame
from herbivorous import *

class Rabbit(Herbivorous):
    def __init__(self,energy,health,sex,radiusView,radiusContact,position):
        Herbivorous.__init__(self,radiusView,radiusContact)
        Living.__init__(self,energy,health,sex)
        self.name = "rabbit"
        self.pregnant = 10
        self.digestion = 10
        self.strength = 1
        self.speed = 7 
        self.position = position
        self.attack = self.energy
    
    #sprite
    def draw(self, position, i):
        gifNumber ='./sprite/Lapin/frame-'+str(i%3+1)+'.gif'
        image = pygame.image.load(gifNumber)
        screen.blit(image, position)

p=0
while p < 10:
    rabbit1=Rabbit(100,300,'male',400,150,position=[random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)])
    rabbit2=Rabbit(100,300,"female",400,150,position=[random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)])
    listeDesHerbivores.append(rabbit1)
    listeDesHerbivores.append(rabbit2)
    p+=1