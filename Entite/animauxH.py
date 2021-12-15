import pygame
from herbivore import *

class lapin(Herbivore):
    def __init__(self,energie,vie,sexe,rayonVision,rayonContact,position):
        Herbivore.__init__(self,rayonVision,rayonContact)
        Vivant.__init__(self,energie,vie,sexe)
        self.name= "lapin"
        self.enceinte = 0
        self.vitesse=5 #vitesse en fonction de l'énergie
        self.position=position
        self.attaque = self.energie
    
    #sprite du bled
    def draw(self, position, i):
        gifNumber='./sprite/Lapin/frame-'+str(i%3+1)+'.gif'
        image = pygame.image.load(gifNumber)
        screen.blit(image, position)


p=0
while p < 10:
    enfant=lapin(30,650,random.choice(['male',"femelle"]),350,50,position=[random.randrange(0,750),random.randrange(0,550)])#self.__class__ permet de récupérer la classe de 'self'
    listeDesHerbivores.append(enfant)
    p+=1