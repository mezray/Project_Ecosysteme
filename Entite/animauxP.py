import pygame
from plante import *

class rose(Plante):
    def __init__(self,energie,vie,sexe,rayonVision,rayonContact,position=[100,100]):
        Plante.__init__(self,rayonVision,rayonContact)
        Vivant.__init__(self,energie,vie,sexe)
        self.vitesse=0 #vitesse en fonction de l'énergie
        self.name = "plante"
        self.position=position
        self.attaque = self.energie
    
    #sprite du bled
    def draw(self, position, i):
        gifNumber='./sprite/pug/frame-'+str(i+1)+'.gif'
        image = pygame.image.load(gifNumber)
        screen.blit(image, position)

p=1
while p < 1:
    enfant=rose(100,100,random.choice(['male',"femelle"]),750,100,position=[random.randrange(0,400),random.randrange(0,300)])#self.__class__ permet de récupérer la classe de 'self'
    listeDesPlantes.append(enfant)
    p+=1 