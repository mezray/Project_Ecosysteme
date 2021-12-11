import pygame
from herbivore import *

class lapin(Herbivore):
    def __init__(self,energie,vie,sexe,rayonVision,rayonContact,position=[100,100], enceinte=0):
        Herbivore.__init__(self,rayonVision,rayonContact)
        Vivant.__init__(self,energie,vie,sexe)
        self.name= "lapin"
        self.enceinte = enceinte
        self.vitesse=7 #vitesse en fonction de l'énergie
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


p=0
while p < 1:
    enfant=lapin(600,0,random.choice(['male',"femelle"]),750,100,position=[random.randrange(0,400),random.randrange(0,300)])#self.__class__ permet de récupérer la classe de 'self'
    listeDesCarnivores.append(enfant)
    p+=1