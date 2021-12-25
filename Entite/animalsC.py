import pygame
from carnivorous import *

class Wolf(Carnivorous):
    def __init__(self,sex,radiusView,radiusContact,position,energy = 150,health = 300):
        Carnivorous.__init__(self,radiusView,radiusContact)
        Living.__init__(self,energy,health,sex)
        self.name = "wolf"
        self.energyMax = 150
        self.healthMax = 300
        self.pregnant = 100
        self.digestion = 500
        self.strength = 1
        self.speed = 7
        self.position = position
        self.attack = self.energy
    
    #sprite
    def draw(self, position, i):
        gifNumber ='./sprite/pug/frame-'+str(i%4+1)+'.gif'
        image = pygame.image.load(gifNumber)
        screen.blit(image, position)


class Cat(Carnivorous):
    def __init__(self,sex,radiusView,radiusContact,position,energy = 50,health = 200):
        Carnivorous.__init__(self,radiusView,radiusContact)
        Living.__init__(self,energy,health,sex)
        self.name = "cat"
        self.energyMax = 50
        self.healthMax = 200
        self.pregnant = 50
        self.digestion = 300
        self.speed = 7
        self.strength = 1
        self.position = position
        self.attack = self.energy
        
    def draw(self, position, i):
        gifNumber ='./sprite/cat/frame-'+str(i+1)+'.gif'
        image = pygame.image.load(gifNumber)
        screen.blit(image, position)

p=0
while p < 1:
    wolf1=Wolf('male',300,150,position=[random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)])
    wolf2=Wolf("female",300,150,position=[random.randrange(100,SCREENWIDTH-100),random.randrange(100,SCREENHEIGHT-100)])
    
    listeDesCarnivores.append(wolf1)
    listeDesCarnivores.append(wolf2)
    p+=1


