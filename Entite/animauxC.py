import pygame
from carnivore import *

class loup(Carnivore):
    def __init__(self,energie,vie,sexe,rayonVision,rayonContact,position=[100,100], enceinte=0):
        Carnivore.__init__(self,rayonVision,rayonContact)
        Vivant.__init__(self,energie,vie,sexe)
        self.name= "loup"
        self.enceinte = enceinte
        self.vitesse=7 #vitesse en fonction de l'énergie
        self.position=position
        self.attaque = self.energie
    
    #sprite du bled
    def draw(self, position, i):
        gifNumber='./sprite/pug/frame-'+str(i%4+1)+'.gif'
        image = pygame.image.load(gifNumber)
        screen.blit(image, position)


class chat(Carnivore):
    def __init__(self,energie,vie,sexe,rayonVision,rayonContact,position=[550,550]):
        Carnivore.__init__(self,rayonVision,rayonContact)
        Vivant.__init__(self,energie,vie,sexe)
        self.name= "chat"
        self.vitesse=7
        self.position=position
        self.attaque = self.energie
        
    def draw(self, position, i):
        gifNumber='./sprite/cat/frame-'+str(i+1)+'.gif'
        image = pygame.image.load(gifNumber)
        screen.blit(image, position)

p=0
while p < 1:
    enfant1=loup(300,300,random.choice(['male',"femelle"]),750,100,position=[random.randrange(0,400),random.randrange(0,300)])#self.__class__ permet de récupérer la classe de 'self'
    enfant2=chat(300,300,random.choice(['male',"femelle"]),750,100,position=[random.randrange(0,400),random.randrange(0,300)])#self.__class__ permet de récupérer la classe de 'self'
    
    listeDesCarnivores.append(enfant1)
    listeDesCarnivores.append(enfant2)
    p+=1


