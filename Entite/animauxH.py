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
        gifNumber='./sprite/Lapin/frame-'+str(i%3+1)+'.gif'
        image = pygame.image.load(gifNumber)
        screen.blit(image, position)


p=0
while p < 1:
    enfant=lapin(600,0,random.choice(['male',"femelle"]),750,100,position=[random.randrange(0,400),random.randrange(0,300)])#self.__class__ permet de récupérer la classe de 'self'
    listeDesCarnivores.append(enfant)
    p+=1