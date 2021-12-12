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
        if i == 0 or i == 3 or i == 6:
            image = pygame.image.load("./sprite/Lapin/frame-1.gif")
            screen.blit(image, position)
        if i == 1 or i == 4 or i == 7:
            image = pygame.image.load("./sprite/Lapin/frame-2.gif")
            screen.blit(image, position)
        if i == 2 or i == 5:
            image = pygame.image.load("./sprite/Lapin/frame-3.gif")
            screen.blit(image, position)


p=0
while p < 1:
    enfant=lapin(600,0,random.choice(['male',"femelle"]),750,100,position=[random.randrange(0,400),random.randrange(0,300)])#self.__class__ permet de récupérer la classe de 'self'
    listeDesCarnivores.append(enfant)
    p+=1